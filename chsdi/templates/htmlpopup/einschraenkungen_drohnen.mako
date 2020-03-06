<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  lang = lang if lang in ('fr', 'it', 'en') else 'de'
  restr = 'restr_%s' % lang
  bew_st = 'bew_st_%s' % lang
  bew_li = 'bew_li_%s' % lang
  name = 'name_%s' % lang
%>
    <tr><td class="cell-left">${h.translate('ch.bazl.einschraenkungen-drohnen.name', lang)}</td>    	<td>${c['attributes'][name] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bazl.einschraenkungen-drohnen.restr', lang)}</td>     <td>${c['attributes'][restr] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bazl.einschraenkungen-drohnen.bew_st', lang)}</td>    <td>${c['attributes'][bew_st] or '-'}</td></tr>
    <td>${h.translate('ch.bazl.einschraenkungen-drohnen.bew_li', lang)}</td>                          <td><a href="${c['attributes'][bew_li]}" target="_blank">${h.translate('ch.bazl.einschraenkungen-drohnen.bew_li_url', lang)}</a>
</%def>

