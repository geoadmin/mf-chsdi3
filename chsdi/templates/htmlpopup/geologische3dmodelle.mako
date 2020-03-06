<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    lang = lang if lang in ('fr','it','en') else 'de'

    contracting_entity = '%s_contracting_entity' %lang
    link_portal = '%s_link_portal' %lang
    %>

    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geologische_3dmodelle.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geologische_3dmodelle.purpose')}</td><td>${c['attributes']['purpose'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geologische_3dmodelle.year_publication')}</td><td>${c['attributes']['year_publication'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_contracting_entity')}</td><td>${c['attributes'][contracting_entity] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_link_portal')}</td>
          % if 'http' not in c['attributes'][link_portal]:
             <td>${c['attributes'][link_portal] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_portal] or '-'}>link</a></td>
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
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.purpose')}</td>
      <td>${c['attributes']['purpose'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.content')}</td>
      <td>${c['attributes']['content'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.remarks')}</td>
      <td>${c['attributes']['remarks'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.year_publication')}</td>
      <td>${c['attributes']['year_publication'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_contracting_entity')}</td>
      <td>${c['attributes'][contracting_entity] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_author')}</td>
      <td>${c['attributes'][author] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_link_portal')}</td>
          % if 'http' not in c['attributes'][link_portal]:
             <td>${c['attributes'][link_portal] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_portal] or '-'}>link</a></td>
          % endif
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_link_description')}</td>
          % if 'http' not in c['attributes'][link_description]:
             <td>${c['attributes'][link_description] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_description] or '-'}>link</a></td>
          % endif
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.swisstopo.geologie-geologische_3dmodelle.de_link_documentation')}</td>
          % if 'http' not in c['attributes'][link_documentation]:
             <td>${c['attributes'][link_documentation] or '-'}</td>
          % else:
             <td><a  target="_blank" href=${c['attributes'][link_documentation] or '-'}>link</a></td>
          % endif
    </tr>
  </table>
</%def>
