<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
      lang = lang if lang in ('fr','it','en') else 'de'
      access_text = 'access_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.linename')}</td>
    <td>${c['attributes']['cubename'] or '-'}</td>
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
    <td class="cell-left">${_('ch.swisstopo.geologie-reflexionsseismik.dim_km2')}</td>
    <td>${c['attributes']['dim_km2'] or '-'}</td>
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
      <td>${c['attributes']['cubename'] or '-'}</td>
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
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.dim_km2')}</td>
      <td>${c['attributes']['dim_km2'] or '-'}</td>
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
      % if c['attributes']['link'] in [None, "-"]:
        <td>${'-'}</td>
      % else:
        <td><a target="_blank" href="${c['attributes']['link']}">${_('link')}</a></td>
      % endif
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.download')}</td>
      <td>${c['attributes']['download'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.swisstopo.geologie-reflexionsseismik.swissgeol')}</td>
      <td>${c['attributes']['swissgeol'] or '-'}</td>
    </tr>
  </table>
</%def>
