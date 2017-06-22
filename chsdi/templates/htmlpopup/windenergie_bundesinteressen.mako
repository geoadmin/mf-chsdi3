<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    kbik = c['attributes']['kbik']
    d_colors = {1:'#8989a0', 2:'#8f0000', 3:'#e34a33', 4:'#fadc8a', 5:'#ffffff'}
    color = d_colors[kbik]
    legend_text = 'ch.are.windenergie-bundesinteressen.bik%s' % kbik
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
    d_langs_bik = {'de':'d','fr':'fr','it':'it','rm':'d','en':'d'}
    lang_bik = d_langs_bik[lang]
    desc_bik1 = c['attributes']['bik1_5_%s' % lang_bik] or '-'
    desc_bik2 = c['attributes']['bik2_%s' % lang_bik] or '-'
    desc_bik3 = c['attributes']['bik3_%s' % lang_bik] or '-'
    desc_bik4 = c['attributes']['bik4_%s' % lang_bik] or '-'

%>
    <body>
    <table class="wind-bund-extended">
       <tr class="wind_info">
            <td colspan="2"><p>${_('ch.are.windenergie-bundesinteressen.tt_info')}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_2"></div><p>${_('ch.are.windenergie-bundesinteressen.bik2')}</p></td>
           <td class="wind_legend"><p>${desc_bik2}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_3"></div><p>${_('ch.are.windenergie-bundesinteressen.bik3')}</p></td>
           <td><p>${desc_bik3}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_4"></div><p>${_('ch.are.windenergie-bundesinteressen.bik4')}</p></td>
           <td><p>${desc_bik4}</p></td>
       </tr>
       <tr class="wind_legend">
           <td><div class="wind_kbik_main wind_kbik_1"></div><div class="wind_kbik_main wind_kbik_5"></div><p>${_('ch.are.windenergie-bundesinteressen.bik1')}, ${_('ch.are.windenergie-bundesinteressen.bik5')}</p></td>
           <td><p>${desc_bik1}</p></td>
       </tr>
       <tr class="wind_info">
           <td colspan="2"><p>${_('ch.are.windenergie-bundesinteressen.tt_info_footer')} <a href="https://${_('ch.are.windenergie-bundesinteressen.tt_link')}" target="_blank">${_('ch.are.windenergie-bundesinteressen.tt_link')}</a></p></td>
       </tr>
    </table>
    </body>
</%def>
