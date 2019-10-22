<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    #schutzs = 'schutzs_%s' % lang
    #bestimmung = 'best_%s' % lang
%>
    <tr><td class="cell-left">Hallo</td>               <td>Welt</td></tr>
</%def>

