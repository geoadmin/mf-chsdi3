<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    kbik = c['attributes']['kbik']
    d_colors = {1:'#B0B0B0', 2:'#A63603', 3:'#E4510C', 4:'#FD8D3C', 5:'#E1E490', 6:'#FFFFFF'}
    d_attr_map = {1:'bauzonen_puffer', 2: 'schutzgeb_o_inter', 3:'grunds_ausschlussgeb', '4': 'inter_abwaeg_national', 5: 'vorbehaltsgeb',  6: 'weitere_einschraenk'}
    color = d_colors[kbik]
    legend_text = 'ch.are.windenergie-bundesinteressen.%s' % d_attr_map[kbik]
%>

<style>
.wind_kbik_dyn {
    border-width: 1px;
    border-style: solid;
    border-color: #999999;
    height: 30px;
    width: 30px;
    margin: 2px 10px 0px 0px;
    float: left;
}

.wind_space {
  height: 15px;
}
.wind_legend_title {
    font-weight: bold;
    height: 20px;
}
</style>

<% c['stable_id'] = False %>
    <tr><td colspan="2">${_('ch.are.windenergie-bundesinteressen.tt_short_info')}</td></tr>
    <tr class="wind_space"><td colspan="2"></td></tr>
    <tr><td class="wind_legend_title" colspan="2">${_('ch.are.windenergie-bundesinteressen.kbik')}:</td></tr>
    <tr><td colspan="2"><div class="wind_bund_extendet.wind_kbik_main wind_kbik_dyn" style="background-color:${color};"></div>${_(legend_text)}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    # get the description
    lang = lang if lang in ('rm','en') else 'de'
    desc_schutzgeb_o_inter = c['attributes']['schutzgeb_o_inter_%s' % lang] or '-'
    desc_grunds_ausschlussgeb = c['attributes']['grunds_ausschlussgeb_%s' % lang] or '-'
    desc_inter_abwaeg_national = c['attributes']['inter_abwaeg_national_%s' % lang] or '-'
    desc_vorbehaltsgeb = c['attributes']['vorbehaltsgeb_%s' % lang] or '-'
    desc_weitere_einschraenk = c['attributes']['weitere_einschraenk_%s' % lang] or '_'

%>
    <body>
    <table class="wind-bund-extended">
       <tr class="wind_info">
            <td colspan="2"><p>${_('ch.are.windenergie-bundesinteressen.tt_info')}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_2"></div><p>${_('ch.are.windenergie-bundesinteressen.schutzgeb_o_inter')}</p></td>
           <td class="wind_legend"><p>${desc_schutzgeb_o_inter}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_3"></div><p>${_('ch.are.windenergie-bundesinteressen.grunds_ausschlussgeb')}</p></td>
           <td><p>${desc_grunds_ausschlussgeb}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_4"></div><p>${_('ch.are.windenergie-bundesinteressen.inter_abwaeg_national')}</p></td>
           <td><p>${desc_inter_abwaeg_national}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_5"></div><p>${_('ch.are.windenergie-bundesinteressen.vorbehaltsgeb')}</p></td>
           <td><p>${desc_vorbehaltsgeb}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_1"></div><div class="wind_kbik_main wind_kbik_6"></div><p>${_('ch.are.windenergie-bundesinteressen.bauzonen_puffer')}, ${_('ch.are.windenergie-bundesinteressen.weitere_einschraenk')}</p></td>
           <td><p>${desc_weitere_einschraenk}</p></td>
       </tr>
       <tr class="wind_info">
           <td colspan="2"><p>${_('ch.are.windenergie-bundesinteressen.tt_info_footer')} <a href="https://${_('ch.are.windenergie-bundesinteressen.tt_link')}" target="_blank">${_('ch.are.windenergie-bundesinteressen.tt_link')}</a></p></td>
       </tr>
    </table>
    </body>
</%def>
