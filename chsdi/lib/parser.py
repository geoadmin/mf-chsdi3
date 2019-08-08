from lark import Lark, Transformer
from lark.exceptions import LarkError
import lark

where_gram = """

?start: value

?value: expressions
     | expression


expressions: expression (and_or expression)* [and_or]

expression: WORD is_not_null
          | WORD operators NUMBERS
          | WORD operators_likes  ESCAPED_QUOTED_STRING

operators: OPERATORS   -> ops
operators_likes: OPERATORS | LIKES

NUMBERS: /(\d+(\.\d+)?)/
WORD: ("_"|LETTER)+

SINGLE_QUOTED_STRING: /'[^']*'/
ESCAPED_QUOTED_STRING: /'(?:[^'\\\\]|\\\\.)*'/
OPERATORS: "<="|">="|"<"|">"|"=="|">="|"<="|"<>"|"!="|"="
LIKES: "ilike"|"not ilike"|"not like"|"like"
OPERATORS_LIKES: OPERATORS | LIKES
and_or: /and|or/i
is_not_null: /is( not)? null/i

%import common.NUMBER
%import common.LETTER
%import common.FLOAT
%import common.INT
%ignore /[\t \f]+/  // WS
"""


class ParseError(Exception):
    pass


class WhereParser(object):

    def __init__(self, text):
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
        except Exception:
            return r
        if isinstance(tr, lark.tree.Tree):
            r = tr.children
        else:
            r.append(tr)

        return r

    def _tree(self):
        tree = []
        try:
            tree = self.parser.parse(self.text)
        except LarkError:
            raise ParseError("Cannot parse '{}'".format(self.text))
        return tree


class WhereTransformer(Transformer):

    def expression(self, args):
        return u" ".join(map(unicode, args))

    def and_or(self, s):
        return unicode(s[0])

    def is_not_null(self, s):
        return unicode(s[0])

    def ops(self, s):
        return str(s[0])

    def operators_likes(self, s):
        return unicode(s[0])
