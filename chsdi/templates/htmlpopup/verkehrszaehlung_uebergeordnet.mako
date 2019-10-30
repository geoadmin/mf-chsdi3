<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.mlocname')}</td> <td>${c['attributes']['mlocname']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.mlocnr')}</td><td>${c['attributes']['mlocnr'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<%
  lang = lang if lang in ('fr','it') else 'de'
  lang = lang if lang != 'it' else 'fr'
  networktype = '%s_networktype' % lang
%>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.mlocname')}</th>
    </tr>
  </table> 

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.mlocname_2')}</td>
      <td>${c['attributes']['mlocname'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.mlocnr')}</td>
      <td>${c['attributes']['mlocnr'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.canton')}</td>
      <td>${c['attributes']['canton'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.streetdesignation')}</td>
      <td>${c['attributes']['streetdesignation'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.targetlocation1')}</td>
      <td>${c['attributes']['targetlocation1'] or '-'}</td>  
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.targetlocation2')}</td>
      <td>${c['attributes']['targetlocation2'] or '-'}</td>  
    </tr> 
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.numberoflanes1')}</td>
      <td>${c['attributes']['numberoflanes1'] or '-'}</td>  
    </tr> 
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.numberoflanes2')}</td>
      <td>${c['attributes']['numberoflanes2'] or '-'}</td>  
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.locationlv95')}</td>
      <td>${c['attributes']['locationlv95'] or '-'}</td>  
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.de_networktype')}</td>
      <td>${c['attributes'][networktype] or '-'}</td> 
 
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.indicator')}</th>
    </tr>
  </table>

  <table class="table-with-border kernkraftwerke-extended">
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.year')}</td>
      <td>${c['attributes']['year'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.dtv')}</td>
      <td>${c['attributes']['dtv'] or '-'}</td>  
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.dwv')}</td>
      <td>${c['attributes']['dwv'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.msp')}</td>
      <td>${c['attributes']['msp'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.asp')}</td>
      <td>${c['attributes']['asp'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.mspw')}</td>
      <td>${c['attributes']['mspw'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.aspw')}</td>
      <td>${c['attributes']['aspw'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.nt')}</td>
      <td>${c['attributes']['nt'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.nn')}</td>
      <td>${c['attributes']['nn'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.prctheavytraffic')}</td>
      <td>${c['attributes']['prctheavytraffic'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.prctheavytrafficday')}</td>
      <td>${c['attributes']['prctheavytrafficday'] or '-'}</td>  
    </tr>       
    <tr>
      <td class="cell-meta">${_('ch.astra.strassenverkehrszaehlung-uebergeordnet.prctheavytrafficnight')}</td>
      <td>${c['attributes']['prctheavytrafficnight'] or '-'}</td>  
    </tr>       
  </table>
</%def>
