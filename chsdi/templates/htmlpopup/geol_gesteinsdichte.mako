<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<tr>
  <td class="cell-left">${_('ch.swisstopo.geologie-gesteinsdichte.saphyr_n')}</td>
  <td class="cell-left">${c['attributes']['saphyr_n'] or '-'}</td>
</tr>

</%def>

