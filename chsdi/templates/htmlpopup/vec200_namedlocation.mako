<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<% c['stable_id'] = True %> 
    <tr><td width="150">${_('name_lang1')}</td><td>${c['attributes']['objname1']}</td></tr>
    <tr><td width="150">${_('name_lang2')}</td><td>
    % if c['attributes']['objname2'].strip() in ['N_P','N_A']:
        -
    % else:
        ${c['attributes']['objname2'] or '-'}
    % endif
    </td></tr>
    <tr><td width="150">${_('hoehe_ueber_meer')}</td><td>${c['attributes']['altitude'] or '-'}</td></tr>
</%def>
