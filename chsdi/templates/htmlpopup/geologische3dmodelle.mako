<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    lang = lang if lang in ('fr','it','en') else 'de'

    contracting_entity = '%s_contracting_entity' %lang
    link_portal = '%s_link_portal' %lang
    %>

    <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.name', lang)}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.purpose', lang)}</td><td>${c['attributes']['purpose'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.year_publication', lang)}</td><td>${c['attributes']['year_publication'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_contracting_entity', lang)}</td><td>${c['attributes'][contracting_entity] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_link_portal', lang)}</td>
          % if 'http' not in c['attributes'][link_portal]:
             <td>${c['attributes'][link_portal] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_portal] or '-'}>Link</a></td>
          % endif
    </tr> 
</%def>

<%def name="extended_info(c, lang)">

    <%
    lang = lang if lang in ('fr','it','en') else 'de'

    contracting_entity = '%s_contracting_entity' %lang
    author =  '%s_author' %lang
    link_portal = '%s_link_portal' %lang
    link_description ='%s_link_description' %lang
    link_documentation = '%s_link_documentation' % lang 
    %>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.name', lang)}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.purpose', lang)}</td>
      <td>${c['attributes']['purpose'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.content', lang)}</td>
      <td>${c['attributes']['content'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.remarks', lang)}</td>
      <td>${c['attributes']['remarks'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.year_publication', lang)}</td>
      <td>${c['attributes']['year_publication'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_contracting_entity', lang)}</td>
      <td>${c['attributes'][contracting_entity] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_author', lang)}</td>
      <td>${c['attributes'][author] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_link_portal', lang)}</td>
          % if 'http' not in c['attributes'][link_portal]:
             <td>${c['attributes'][link_portal] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_portal] or '-'}>Link</a></td>
          % endif
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_link_description', lang)}</td>
          % if 'http' not in c['attributes'][link_description]:
             <td>${c['attributes'][link_description] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_description] or '-'}>Link</a></td>
          % endif
    </tr>
    <tr>
      <td class="cell-meta">${h.translate('ch.swisstopo.geologie-geologische_3dmodelle.de_link_documentation', lang)}</td>
          % if 'http' not in c['attributes'][link_documentation]:
             <td>${c['attributes'][link_documentation] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_documentation] or '-'}>Link</a></td>
          % endif
    </tr>
  </table>
</%def>
