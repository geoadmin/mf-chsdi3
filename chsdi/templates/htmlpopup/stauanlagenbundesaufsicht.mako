<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it','en') else 'de'
    lang = lang if lang != 'it' else 'fr'
    damtype = 'damtype_%s' % lang
%>
    <tr><td class="cell-left">${Translator.translate('ch.bfe.stauanlagen-bundesaufsicht.damname', lang)}</td>              <td>${c['attributes']['damname']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('baujahr', lang)}</td>                                                <td>${c['attributes']['baujahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_damtype', lang)}</td>           <td>${c['attributes'][damtype] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_damheight', lang)}</td>         <td>${int(c['attributes']['damheight']) or '-'}&nbsp;m</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_crestlevel')}</td>        <td>${int(c['attributes']['crestlevel']) or '-'}&nbsp;${_('abk_meter_ueber_meer', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_crestlength', lang)}</td>       <td>${int(c['attributes']['crestlength']) or '-'}&nbsp;m</td></tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
        c['stable_id'] = True
        lang = lang if lang in ('fr','it','en') else 'de'
        lang = lang if lang != 'it' else 'fr'
        damtype = 'damtype_%s' % lang
        img_url = "//www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.stauanlagen-bundesaufsicht/"+str(c['attributes']['facility_stabil_id'])+".jpg"
        image_exist = h.resource_exists('http:' + img_url)
    %>
    <h1>${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_stauanlage', lang)} ${c['attributes']['facilityname']}</h1>
    <table class="table-with-border kernkraftwerke-extended">
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_stauanlage', lang)}</th>
            <td>${c['attributes']['facilityname']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('baujahr', lang)}</th>
            <td>${c['attributes']['baujahr'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_inbetriebabnahme', lang)}</th>
            <td>${c['attributes']['beginningofoperation']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_zweck', lang)}</th>
            <td>${c['attributes']['facaim_'+lang]}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_aufsichtstart', lang)}</th>
            <td>${c['attributes']['startsupervision']}</td>
        </tr>
        <tr>
            <td colspan="2">&nbsp;</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_stauraum', lang)}</th>
            <td>${c['attributes']['reservoirname']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_stauraumvolume', lang)} [Mio m<sup>3</sup>]</th>
            <td>${c['attributes']['impoundmentvolume']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_stauzielskote')} [${_('abk_meter_ueber_meer', lang)}]</th>
            <td>${c['attributes']['impoundmentlevel']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_stauhoehe', lang)} [m]</th>
            <td>${c['attributes']['storagelevel']}</td>
        </tr>
        <tr>
            <td colspan="2">&nbsp;</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_sperre', lang)}</th>
            <td>${c['attributes']['damname']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_damheight', lang)} [m]</th>
            <td>${c['attributes']['damheight']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_crestlevel')} [${_('abk_meter_ueber_meer', lang)}]</th>
            <td>${c['attributes']['crestlevel']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_crestlength', lang)} [m]</th>
            <td>${c['attributes']['crestlength']}</td>
        </tr>
        <tr>
            <th class="cell-left">${Translator.translate('tt_ch.bfe.stauanlagen-bundesaufsicht_damtype', lang)}</th>
            <td>${c['attributes'][damtype]}</td>
        </tr>
    </table>
    % if image_exist:
    <div class="thumbnail-container">
        <div class="thumbnail">
             <a href="${img_url}" target="_blank"><img class="image" src="${img_url}" alt=""/></a>
        </div>
    </div>
    % endif
</%def>
