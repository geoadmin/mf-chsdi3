<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it') else 'de'
    standorttyp = 'standorttyp_%s' % lang
    statusaltlv = 'statusaltlv_%s' % lang
    untersuchungsmassnahmen = 'untersuchungsmassnahmen_%s' % lang
    str_output = c['attributes'][untersuchungsmassnahmen].replace('##', '<br />')
%>

    <tr><td class="cell-left">${_('ch.vbs.kataster-belasteter-standorte-militaer.katasternummer')}</td>                        <td>${c['attributes']['katasternummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.kataster-belasteter-standorte-militaer.standorttyp')}</td>                           <td>${c['attributes'][standorttyp] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.kataster-belasteter-standorte-militaer.status_altlv')}</td>                          <td>${c['attributes'][statusaltlv] or '-'}</td></tr>
    <tr><td class="cell-left" valign="top">${_('ch.vbs.kataster-belasteter-standorte-militaer.untersuchungsmassnahmen')}</td>  <td>${_(str_output)|n}</td></tr> 
    <tr><td class="cell-left">${_('ch.vbs.kataster-belasteter-standorte-militaer.url_kbs_auszug')}</td>                        <td><a href="${c['attributes']['url'] or '-'}" target="_blank">${_('link')}</a></td></tr>

</%def>
