<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bfe.meteorologische-vereisung.vereisung')}</td>    <td>${c['attributes']['vereisung']}%</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.meteorologische-vereisung.hoehe')}</td>    <td>${c['attributes']['hoehe']}</td></tr>
</%def>
