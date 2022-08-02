<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    zone_name = 'zone_name_%s' % lang
    zone_restriction = 'zone_restriction_%s' % lang
    zone_message = 'zone_message_%s' % lang
    auth_url = 'auth_url_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_name')}</td>
    <td>${c['attributes'][zone_name] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_restriction')}</td>
    <td>${c['attributes'][zone_restriction] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_message')}</td>
    <td>${c['attributes'][zone_message] or '-'}</td>
  </tr>
  <tr>
    <td>${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_url')}</td>
    <td><a href="${c['attributes'][auth_url]}" target="_blank">${_('link')}</a>
  </tr>
</%def>

<%def name="extended_info(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    zone_name = 'zone_name_%s' % lang
    zone_restriction = 'zone_restriction_%s' % lang
    zone_message = 'zone_message_%s' % lang
    auth_url = 'auth_url_%s' % lang
    auth_name = 'auth_name_%s' % lang
    auth_contact = 'auth_contact_%s' % lang
    auth_service = 'auth_service_%s' % lang
    auth_email = 'auth_email_%s' % lang
    auth_phone = 'auth_phone_%s' % lang
    period_end = ','.join(c['attributes']['period_end']) if c['attributes']['period_end'] else '-'
  %>
  <table>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_name')}</td>
      <td class="cell-meta">${c['attributes'][zone_name] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_restriction')}</td>
      <td class="cell-meta">${c['attributes'][zone_restriction] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_message')}</td>
      <td class="cell-meta">${c['attributes'][zone_message] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_url')}</td>
      <td class="cell-meta"><a href="${c['attributes'][auth_url]}" target="_blank">${_('link')}</a>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_name')}</td>
    <td class="cell-meta">${c['attributes'][auth_name] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_service')}</td>
    <td class="cell-meta">${c['attributes'][auth_service] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_contactname')}</td>
    <td class="cell-meta">${c['attributes'][auth_contact] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_email')}</td>
    <td class="cell-meta">${c['attributes'][auth_email] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_phone')}</td>
    <td class="cell-meta">${c['attributes'][auth_phone] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_intervalbefore')}</td>
    <td class="cell-meta">${c['attributes']['auth_intervalbefore'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_lowerlimit')}</td>
    <td class="cell-meta">${c['attributes']['air_vol_lower_vref'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_upperlimit')}</td>
    <td class="cell-meta">${c['attributes']['air_vol_upper_limit'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_lowervref')}</td>
    <td class="cell-meta">${c['attributes']['air_vol_lower_vref'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_uppervref')}</td>
    <td class="cell-meta">${c['attributes']['air_vol_upper_vref'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.time_permanent')}</td>
    <td class="cell-meta">${c['attributes']['time_permanent'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.time_start')}</td>
    <td class="cell-meta">${c['attributes']['time_start'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.time_end')}</td>
    <td class="cell-meta">${c['attributes']['time_end'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.period_day')}</td>
    <td class="cell-meta">${c['attributes']['period_day'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.period_start')}</td>
    <td class="cell-meta">${c['attributes']['period_start'] or '-'}</td>
    </tr>
    <tr>
    <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.period_end')}</td>
    <td class="cell-meta">${_(period_end)}</td>
    </tr>
  </table>
</%def>
