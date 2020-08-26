<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
    objekt_text = 'objekt_%s' % lang[0]
%>

<tr>
  <td class="cell-left">${_('ch.blw.ursprungsbezeichnungen.objektcode')}</td>
  <td class="cell-left">${c['attributes']['objektcode'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.blw.ursprungsbezeichnungen.objekt')}</td>
  <td class="cell-left">${c['attributes'][objekt_text] or '-'}</td>
</tr>

</%def>
