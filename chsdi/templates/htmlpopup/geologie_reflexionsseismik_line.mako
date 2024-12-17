<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
      lang = lang if lang in ('fr','it','en') else 'de'
      access_text = 'access_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.linename')}</td>
    <td>${c['attributes']['linename'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.alias')}</td>
    <td>${c['attributes']['alias'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.survey')}</td>
    <td>${c['attributes']['survey'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.dim_km')}</td>
    <td>${c['attributes']['dim_km'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.access')}</td>
    <td>${c['attributes'][access_text] or '-'}</td>
  </tr>
</%def>

<%def name="extended_info(c, lang)">
  <%
      lang = lang if lang in ('fr','it','en') else 'de'
      access_text = 'access_%s' % lang
      domain_text = 'domain_%s' % lang
  %>
  <table class="table-with-border" cellpadding="5">
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.linename')}</td>
      <td>${c['attributes']['linename'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.alias')}</td>
      <td>${c['attributes']['alias'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.survey')}</td>
      <td>${c['attributes']['survey'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.dim_km')}</td>
      <td>${c['attributes']['dim_km'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.access')}</td>
      <td>${c['attributes'][access_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.reference')}</td>
      <td>${c['attributes']['reference'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.srd')}</td>
      <td>${c['attributes']['srd'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.domain')}</td>
      <td>${c['attributes'][domain_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.vintage')}</td>
      <td>${c['attributes']['vintage'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.owner')}</td>
      <td>${c['attributes']['owner'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.region')}</td>
      <td>${c['attributes']['region'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.link')}</td>
      % if c['attributes']['link'] and c['attributes']['link'].startswith('http'):
        <td><a href="${c['attributes']['link']}" target="_blank">${_('link')}</a></td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.download')}</td>
      % if c['attributes']['download'] and c['attributes']['download'].startswith('http'):
        <td><a href="${c['attributes']['download']}" target="_blank">${_('link')}</a></td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.swissgeol')}</td>
      % if c['attributes']['swissgeol'] and c['attributes']['swissgeol'].startswith('http'):
        <td><a href="${c['attributes']['swissgeol']}" target="_blank">${_('link')}</a></td>
      % else:
        <td>-</td>
      % endif
    </tr>
  </table>
</%def>
