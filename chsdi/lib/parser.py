import six
from lark import Lark, Transformer
from lark.exceptions import LarkError
import lark
import logging

if six.PY3:
    unicode = str

log = logging.getLogger(__name__)

where_gram = """

?start: value

?value: expressions
     | expression


expressions: expression (and_or expression)* [and_or]

expression: WORD is_not_null
          | WORD IS_NOT BOOLEAN
          | WORD operators SIGNED_NUMBER
          | WORD operators_likes  ESCAPED_QUOTED_STRING

operators: OPERATORS   -> ops
operators_likes: OPERATORS | LIKES

NUMBERS: /(\d+(\.\d+)?)/
// WORD must and may only be a valid python variable name:
// - first character must be one of [_,a-z,A-Z]
// - other character may be one of [_,a-z,A-Z,0-9]
WORD: ("_"|LETTER)("_"|LETTER|NUMBER)*

SINGLE_QUOTED_STRING: /'[^']*'/
ESCAPED_QUOTED_STRING: /'(?:[^'\\\\]|\\\\.)*'/
OPERATORS: "<="|">="|"<"|">"|">="|"<="|"!="|"="
LIKES: "ilike"|"not ilike"|"not like"|"like"
OPERATORS_LIKES: OPERATORS | LIKES
BOOLEAN: "true" | "false"
and_or: /and|or/i
is_not_null: /is( not)? null/i
IS_NOT: "is not"|"!="|"="|"is"

%import common.NUMBER
%import common.SIGNED_NUMBER
%import common.LETTER
%import common.FLOAT
%import common.INT
%ignore /[\t \f]+/  // WS
"""


class ParseError(Exception):
    pass


class WhereParser(object):

    def __init__(self, text):
        log.debug(u'WhereParser string to parse: {}'.format(unicode(text)))

        self.text = text
        self.parser = Lark(where_gram, debug=True)
        self.transformer = WhereTransformer()

    @property
    def sql(self):
        tokens = self._tokens()
        if len(tokens) < 1:
            return None
        return u" ".join(tokens)

    @property
    def tokens(self):
        return filter(lambda x: x not in ('or', 'and'), self._tokens())

    @property
    def operators(self):
        return filter(lambda x: x in ('or', 'and'), self._tokens())

    def _tokens(self):
        r = []
        try:
            tr = self.transformer.transform(self._tree())
        except Exception as e:
            log.debug(e)
            return r
        if isinstance(tr, lark.tree.Tree):
            r = tr.children
        else:
            r.append(tr)
        # log.debug(u'tokens: {}'.format(unicode(r)))
        return r

    def _tree(self):
        tree = []
        try:
            tree = self.parser.parse(self.text)
        except LarkError as e:
            raise ParseError("Cannot parse '{}': {}".format(self.text, e))
        # log.debug(u'tree: {}'.format(unicode(tree)))
        return tree


class WhereTransformer(Transformer):

    def expression(self, args):
        return u" ".join(map(unicode, args))

    def and_or(self, s):
        # log.debug(u'and_or: {}'.format(unicode(s[0]).lower()))
        return unicode(s[0]).lower()

    def is_not_null(self, s):
        return unicode(s[0]).lower()

    def ops(self, s):
        return str(s[0]).lower()

    def operators_likes(self, s):
        return unicode(s[0]).lower()

    def BOOLEAN(self, s):
        # log.debug(u'boolean: {}'.format(unicode(s)))
        return "true" == str(s[0]).lower()

    def IS_NOT(self, s):
        return unicode(s[0]).lower()
