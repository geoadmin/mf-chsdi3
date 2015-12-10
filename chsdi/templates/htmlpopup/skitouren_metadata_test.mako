<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
   lang = lang if lang in ('fr','it','en') else 'de'
%>

<%
   fid = str(c['featureId'])
   image = "https://dav0.bgdi.admin.ch/swisstopoproducts/110/" + fid + ".jpg"
%>


    <tr><td class="cell-left">${_('kartenblatt')}</td>         <td>${c['featureId']} ${c['attributes']['name']}<td><td rowspan="6"><img
    src="${image}"/></{{td></tr>
    <tr><td class="cell-left">${_('datenstand')}</td>          <td>${c['attributes']['legendecms2007']}<td></tr>
    <tr height="100"><td class="cell-left">${_('preis')}</td>               <td>${c['attributes']['preis']}</td></tr>
</%def>
