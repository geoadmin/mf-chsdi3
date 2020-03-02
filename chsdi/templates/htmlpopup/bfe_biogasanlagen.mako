<%inherit file="base.mako"/>

<%def name="biogas_production_graph(data)">
    <style>
        #biogas_plant_production_graph img {
            max-width: 100%;
        }
        #biogas_plant_production_graph label {
            font-weight: 700;
        }
    </style>
    <div id="biogas_plant_production_graph">
        <label>${t.Translator.translate('ch.bfe.biogasanlagen.powergeneration', lang)}</label>
        <img src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.biogasanlagen/plot${data['plant_id']}.png">
    </div>
</%def>

<%def name="table_body(c, lang)">
<%
    langWithFallback = lang
    if langWithFallback == 'rm':
        langWithFallback = 'de'

    data = c['attributes']
%>
    <style>
        #biogas_plant_production_graph {
            text-align: center;
        }
        #biogas_plant_production_graph label {
            width: 100%;
            text-align: left;
        }
        #biogas_plant_production_graph img {
            max-height: 200px;
        }
    </style>
    <tr>
        <td class="cell-left"><label>${_('ch.bfe.biogasanlagen.name' )}</label></td>
        <td>${data['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left"><label>${t.Translator.translate('ch.bfe.biogasanlagen.operator', lang)}</label></td>
        <td>${data['operator'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left"><label>${t.Translator.translate('ch.bfe.biogasanlagen.facilitykind', lang)}</label></td>
        <td>${data['facilitykind_' + langWithFallback] or '-'}</td>
    </tr>
    <tr>
        <td colspan="2">${biogas_production_graph(data)}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    langWithFallback = lang
    if langWithFallback == 'rm':
        langWithFallback = 'de'

    data = c['attributes']
%>
    <table class="table-with-border">
        <tr>
            <th class="cell-left">${_('ch.bfe.biogasanlagen.name' )}</th>
            <td>${data['name'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.place', lang)}</th>
            <td>${data['place'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.operator', lang)}</th>
            <td>${data['operator'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.beginingofoperation', lang)}</th>
            <td>${data['beginingofoperation'] or '-'}</td>
        </tr>
% if data['web'] != None:
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.web', lang)}</th>
            <td>
                <a target="_blank" href="${data['web']}">${data['web']}</a>
            </td>
        </tr>
% endif
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.combinedheatandpower', lang)}</th>
            <td>${data['combinedheatandpower'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.upgradingcapacity', lang)}</th>
            <td>${data['upgradingcapacity'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.facilitykind', lang)}</th>
            <td>${data['facilitykind_' + langWithFallback] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.upgradingtechnology', lang)}</th>
            <td>${data['upgradingtechnology_' + langWithFallback] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.valorizationtype', lang)}</th>
            <td>${data['valorizationtype_' + langWithFallback] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${t.Translator.translate('ch.bfe.biogasanlagen.feedback', lang)}</th>
            <td><a target="_blank" href="https://www.uvek-gis.admin.ch/BFE/storymaps/EE_Biogas_Feedbackformular/?name=${data['name']}&ort=${data['place']}&long=${c['geometry']['coordinates'][0]}&lat=${c['geometry']['coordinates'][1]}&lang=${lang}">${t.Translator.translate('ch.bfe.biogasanlagen.sendfeedback', lang)}</a></td>
        </tr>
        <tr>
            <td colspan="2">${biogas_production_graph(data)}</td>
        </tr>
    </table>
</%def>
