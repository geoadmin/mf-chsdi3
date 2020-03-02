<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    import datetime
    lang = lang if lang in ('fr','it','de') else 'de'
    description = 'description_%s' % lang
    datefrom = datetime.datetime.strptime(c['attributes']['valid_from'].strip(), "%Y%m%d").strftime("%d.%m.%Y")

%>
    <tr><td class="cell-left">${Translator.translate('ch.bav.sachplan-infrastruktur-schiene_ausgangslage.name', lang)}</td>         <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.sachplan-infrastruktur-schiene_ausgangslage.description_de', lang)}</td>              <td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_sachplan-infrastruktur-schiene_aus_anlageart', lang)}</td>      <td>${c['attributes']['fackind'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.energieforschung_projektstatus', lang)}</td>             <td>${c['attributes']['facstatus'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_sachplan-infrastruktur-schiene_aus_validform', lang)}</td>      <td>${datefrom or '-'}</td></tr>
</%def>
