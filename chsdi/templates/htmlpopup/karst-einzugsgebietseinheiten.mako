<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%  
    c['stable_id'] = True
    lang = lang if lang in ('fr','it','en') else 'de'
    ub_type = 'ub_type_%s' % lang
%>
<% shape_area_in_km2 = round(c['attributes']['shape_area'] / 1000000, 1) if c['attributes']['shape_area'] else 0 %>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-einzugsgebietseinheiten.ub_type', lang)}</td>           <td>${c['attributes'][ub_type] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-einzugsgebietseinheiten.ub_flux', lang)}</td>           <td>${c['attributes']['ub_flux_fr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-einzugsgebietseinheiten.shape_area', lang)}</td>        <td>${shape_area_in_km2 or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-einzugsgebietseinheiten.ub_alt_min', lang)}</td>        <td>${c['attributes']['ub_alt_min'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-einzugsgebietseinheiten.ub_alt_moy', lang)}</td>        <td>${c['attributes']['ub_alt_moy'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-einzugsgebietseinheiten.ub_alt_max', lang)}</td>        <td>${c['attributes']['ub_alt_max'] or '-'}</td></tr>
</%def>

