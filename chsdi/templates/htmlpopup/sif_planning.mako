<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    import datetime
    lang = lang if lang in ('fr','it') else 'de'
    plname = 'plname_%s' % lang
    datefrom = datetime.datetime.strptime(c['attributes']['validfrom'].strip(), "%Y-%m-%d").strftime("%d.%m.%Y")
%>
    <tr><td class="cell-left">${_('tt_sachplan_facility_name')}</td>             <td>${c['attributes'][plname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_beschlussdatum')}</td>   <td>${datefrom or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>
    % if c['attributes']['doc_web']:
        <td><a href="${c['attributes']['doc_web']}" target="_blank">${c['attributes']['doc_title'] or '-'}</a></td></tr>
    % else:
        <td> - </td></tr>
    %endif
</%def>
