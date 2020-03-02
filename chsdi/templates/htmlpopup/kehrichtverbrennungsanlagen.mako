<%inherit file="base.mako"/>

<%def name="kehrichtverbrennungsanlagen_waerme_graph(data)">
    <style>
        #kehrichtverbrennungsanlagen_waerme_graph img {
            max-width: 100%;
        }
        #kehrichtverbrennungsanlagen_waerme_graph label {
            font-weight: 700;
        }
    </style>
    <div id="kehrichtverbrennungsanlagen_waerme_graph">
        <label>${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.diagramm_waerme', lang)}</label>
        <img src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.kehrichtverbrennungsanlagen/waerme_${c['attributes']['wasteincinerationplantr']}.png">
    </div>
</%def>

<%def name="kehrichtverbrennungsanlagen_strom_graph(data)">
    <style>
        #kehrichtverbrennungsanlagen_strom_graph img {
            max-width: 100%;
        }
        #kehrichtverbrennungsanlagen_strom_graph label {
            font-weight: 700;
        }
    </style>
    <div id="kehrichtverbrennungsanlagen_strom_graph">
        <label>${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.diagramm_strom', lang)}</label>
        <img src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.kehrichtverbrennungsanlagen/strom_${c['attributes']['wasteincinerationplantr']}.png">
    </div>
</%def>

<%def name="table_body(c, lang)">
    <style>
        #kehrichtverbrennungsanlagen_waerme_graph {
            text-align: center;
        }
        #kehrichtverbrennungsanlagen_waerme_graph label {
            width: 100%;
            text-align: left;
        }
        #kehrichtverbrennungsanlagen_waerme_graph img {
            max-height: 200px;
        }
    </style>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.name', lang)}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.place', lang)}</td>
        <td>${c['attributes']['place'] or '-'}</td>
    </tr>
%if c['attributes']['web']:
    <tr>
        <td>${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.web', lang)}</td>
        <td><a href="${c['attributes']['web']}" target="_blank">${c['attributes']['web']}</a></te>
    </tr>
%else:
    <tr>
        <td>${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.web', lang)}</td>
        <td> - </td>
    </tr>
%endif
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.beginning_of_operation', lang)}</td>
        <td>${c['attributes']['beginningofoperation'] or '-'}</td>
    </tr>
    <tr>
        <td colspan="2">${kehrichtverbrennungsanlagen_waerme_graph(c['attributes'])}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">

    <table class="table-with-border">
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.name' , lang)}</th>
            <td>${c['attributes']['name'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.place', lang)}</th>
            <td>${c['attributes']['place'] or '-'}</td>
        </tr>
    %if c['attributes']['web']:
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.web', lang)}</th>
            <td>
                <a target="_blank" href="${c['attributes']['web']}">${c['attributes']['web']}</a>
            </td>
        </tr>
    %else:
        <tr>
            <td>${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.web', lang)}</td>
            <td> - </td>
        </tr>
    %endif
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.kehrichtverbrennungsanlagen.beginning_of_operation', lang)}</th>
            <td>${c['attributes']['beginningofoperation'] or '-'}</td>
        </tr>
        <tr>
            <td colspan="2">${kehrichtverbrennungsanlagen_waerme_graph(c['attributes'])}</td>
        </tr>
        <tr>
            <td colspan="2">${kehrichtverbrennungsanlagen_strom_graph(c['attributes'])}</td>
        </tr>
    </table>
</%def>
