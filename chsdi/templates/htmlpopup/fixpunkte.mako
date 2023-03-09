<%inherit file="base.mako"/>

<%def name="translate_attribute(attribute, value)">
<%
    if value is None:
      return '-'
    else:
      result =  _(u'{}.{}.{}'.format(c['layerBodId'], attribute, value))
      return value if c['layerBodId'] in result else result
%>
</%def>
<%def name="format_coord(coord)">
<%
    if coord is None:
      return '-'
    else:
      arr_coord = coord.split('/')
      if len(arr_coord) == 2:
        easting = '{0:.3f}'.format(float(arr_coord[0]))
        northing = '{0:.3f}'.format(float(arr_coord[1]))
        coord = '{} / {}'.format(easting, northing)
      return coord 
%>
</%def>
<%def name="format_alti(alti)">
<%
    if alti is None:
      return '-'
    return '{0:.3f}'.format(alti)
%>
</%def>


<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
	<tr><td class="cell-left">${_(c['layerBodId']+'.id')}</td>						<td>${c['featureId']}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.status')}</td>      			<td>${_(translate_attribute('status', c['attributes']['status']))}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.koordinate')}</td>      		<td>${format_coord(c['attributes']['koordinate'])}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.hoehe_geom_m')}</td>      		<td>${format_alti(c['attributes']['hoehe_geom_m'])}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.url_punktprotokoll')}</td>      <td><a href="${c['attributes']['url_punktprotokoll'] or '-'}" target="_blank">${_(c['layerBodId']+'.url_punktprotokoll')}</a></td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.punktzeichen')}</td>      		<td>${_(translate_attribute('punktzeichen', c['attributes']['punktzeichen']))}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.kanton')}</td>      			<td>${c['attributes']['kanton'] or '-'}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.zust_name')}</td>      			<td>${c['attributes']['zust_name'] or '-'}</td></tr>
</%def>
