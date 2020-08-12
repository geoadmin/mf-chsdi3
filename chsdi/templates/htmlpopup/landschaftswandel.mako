<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it', 'en') else 'de'
    typ1 = 'typ1_%s' % lang
    typ2 = 'typ2_%s' % lang
    typ3 = 'typ3_%s' % lang
    typ4 = 'typ4_%s' % lang
%>

<tr><td class="cell-left">${_('ch.bfs.landschaftswandel.gmde')}</td><td>${c['attributes']['gmde'] or '-'}</td></tr>

<tr><td class="cell-left">${_('ch.bfs.landschaftswandel.swissnames')}</td><td colspan="4">${c['attributes']['swissnames'] or '-'}</td></tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ1')}</td>
  <td>${c['attributes']['typ1'] or '-'}</td>
  <td>${c['attributes']['typ2'] or '-'}</td>
  <td>${c['attributes']['typ3'] or '-'}</td>
  <td>${c['attributes']['typ4'] or '-'}</td>
</tr>

</%def>

