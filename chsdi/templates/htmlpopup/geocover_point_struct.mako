<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = 'de' if lang in ('de', 'rm', 'en') else 'fr'
    description = 'description_%s' % lang
    spec_description = 'spec_description_%s' % lang
%>
    <tr><td class="cell-left">${_('geocover_description')}</td><td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_polarity')}</td><td>${c['attributes'][spec_description] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_strike')}</td><td>${c['attributes']['azimut'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_dip')}</td><td>${c['attributes']['dip'] or '-'}</td></tr>
    <tr>
        <td class="cell-left">${_('geocover_erl_num')}</td>
        % if c['attributes']['erl_num']:
        <td><a target ="_blank" href="${c['attributes']['erl_num']}">${_('link')}</a></td>
        % else:
        <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('geocover_ber_num')}</td>
        % if c['attributes']['ber_num']:
        <td><a target ="_blank" href="${c['attributes']['ber_num']}">${_('link')}</a></td>
        % else:
        <td>-</td>
        % endif
    </tr>
</%def>
