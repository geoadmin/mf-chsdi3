<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it') else 'de'
    zustand = 'zustand_%s' % lang

%>

    <tr><td class="cell-left">${_('ch.bafu.fauna-wildtierkorridor_national.objnummer')}</td>       <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.fauna-wildtierkorridor_national.name')}</td>            <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.fauna-wildtierkorridor_national.zustand')}</td>         <td>${c['attributes'][zustand] or '-'}</td></tr>
    <tr><td class="cell-left">${_('pdf')}</td>          <td>
    % if c['attributes']['ref_obj_blat']:
      <a href="${c['attributes']['ref_obj_blat']}" target="_blank">${_('link')}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>

