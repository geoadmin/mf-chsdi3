<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
%>

    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege')}</td>                              <td>hallo</td></tr>
    <tr><td class="cell-left">${_('link')}</td>                                                       <td>Welt</td></tr>
</%def>

