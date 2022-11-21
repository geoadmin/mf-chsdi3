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
    <td><a href="${c['attributes'][auth_url]}" target="_blank">${_('ch.bazl.gebietsbeschraenkungen-drohnen.link')}</a>
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
    auth_service = 'auth_service_%s' % lang
    auth_url_txt = ' / '.join(c['attributes'][auth_url]) if c['attributes'][auth_url] else '-'
    auth_name_txt = ' / '.join(c['attributes'][auth_name]) if c['attributes'][auth_name] else '-'
    auth_service_txt = ' / '.join(c['attributes'][auth_service]) if c['attributes'][auth_service] else '-'
    auth_contact = ' / '.join(c['attributes']['auth_contact']) if c['attributes']['auth_contact'] else '-'
    auth_email = ' / '.join(c['attributes']['auth_email']) if c['attributes']['auth_email'] else '-'
    auth_phone = ' / '.join(c['attributes']['auth_phone']) if c['attributes']['auth_phone'] else '-'
    auth_intervalbefore = ' / '.join(c['attributes']['auth_intervalbefore']) if c['attributes']['auth_intervalbefore'] else '-'
    period_day = ' / '.join(c['attributes']['period_day']) if c['attributes']['period_day'] else '-'
    period_start = ' / '.join(c['attributes']['period_start']) if c['attributes']['period_start'] else '-'
    period_end = ' / '.join(c['attributes']['period_end']) if c['attributes']['period_end'] else '-'
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
      <td class="cell-meta"><a href="${_(auth_url_txt)}" target="_blank">${_('ch.bazl.gebietsbeschraenkungen-drohnen.link')}</a>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_name')}</td>
      <td class="cell-meta">${_(auth_name_txt)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_service')}</td>
      <td class="cell-meta">${_(auth_service_txt)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_contactname')}</td>
      <td class="cell-meta">${_(auth_contact)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_email')}</td>
      <td class="cell-meta">${_(auth_email)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_phone')}</td>
      <td class="cell-meta">${_(auth_phone)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_intervalbefore')}</td>
      <td class="cell-meta">${_(auth_intervalbefore)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_lowerlimit')}</td>
      <td class="cell-meta">${c['attributes']['air_vol_lower_limit'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_lowervref')}</td>
      <td class="cell-meta">${c['attributes']['air_vol_lower_vref'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.air_upperlimit')}</td>
      <td class="cell-meta">${c['attributes']['air_vol_upper_limit'] or '-'}</td>
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
      <td class="cell-meta">${_(period_day)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.period_start')}</td>
      <td class="cell-meta">${_(period_start)}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.period_end')}</td>
      <td class="cell-meta">${_(period_end)}</td>
    </tr>
  </table>
</%def>
