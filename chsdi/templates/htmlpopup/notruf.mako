<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>

    <tr><td class="cell-left">${t.Translator.translate('ch.bakom.notruf.name', lang)}</td>    	<td>${c['attributes']['name'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<%
    def text_separation(arr_titles):
        arr_test = arr_titles.split('\n')
        arr_len = len(arr_test)
        str_output = ''
        for i in range(arr_len):
            str_output = str_output + arr_test[i] + '<br />' if  i < (arr_len-1) else str_output + arr_test[i]
        endfor
        return str_output

    arr_fn_addresse_112 = c['attributes']['fn_addresse_112']
    arr_fn_addresse_117 = c['attributes']['fn_addresse_117']
    arr_fn_addresse_118 = c['attributes']['fn_addresse_118']
    arr_fn_addresse_143 = c['attributes']['fn_addresse_143']
    arr_fn_addresse_144 = c['attributes']['fn_addresse_144']
    arr_fn_addresse_147 = c['attributes']['fn_addresse_147']
    arr_mo_addresse_112 = c['attributes']['mo_addresse_112']
    arr_mo_addresse_117 = c['attributes']['mo_addresse_117']
    arr_mo_addresse_118 = c['attributes']['mo_addresse_118']
    arr_mo_addresse_143 = c['attributes']['mo_addresse_143']
    arr_mo_addresse_144 = c['attributes']['mo_addresse_144']
    arr_mo_addresse_147 = c['attributes']['mo_addresse_147']
    arr_sa_addresse_112 = c['attributes']['sa_addresse_112']

    fn_addresse_112 = text_separation(arr_fn_addresse_112)
    fn_addresse_117 = text_separation(arr_fn_addresse_117)
    fn_addresse_118 = text_separation(arr_fn_addresse_118)
    fn_addresse_143 = text_separation(arr_fn_addresse_143)
    fn_addresse_144 = text_separation(arr_fn_addresse_144)
    fn_addresse_147 = text_separation(arr_fn_addresse_147)
    mo_addresse_112 = text_separation(arr_mo_addresse_112)
    mo_addresse_117 = text_separation(arr_mo_addresse_117)
    mo_addresse_118 = text_separation(arr_mo_addresse_118)
    mo_addresse_143 = text_separation(arr_mo_addresse_143)
    mo_addresse_144 = text_separation(arr_mo_addresse_144)
    mo_addresse_147 = text_separation(arr_mo_addresse_147)
    sa_addresse_112 = text_separation(arr_sa_addresse_112)
%>

<table class="table-with-border">
    <colgroup>
      <col width=65%>
      <col width=40%>
      <col width=60%>
      <col width=80%>
    </colgroup>
    <tr><th class="cell-meta" colspan="4">${112}</th></tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.festnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['festnetz_112'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_112_festnetz', lang)}</th>
        <td class="cell-meta">${_(fn_addresse_112)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.mobilnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['mobile_112'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_112_mobil', lang)}</th>
        <td class="cell-meta">${_(mo_addresse_112)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.satellit', lang)}</th>
        <td class="cell-meta">${c['attributes']['satellit_112'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_112_satellit', lang)}</td>
        <td class="cell-meta">${_(sa_addresse_112)|n}</td>
    </tr>
</table>
<tr><td class="cell-meta-one" colspan="2">&nbsp;</td></tr>
<table class="table-with-border">
    <colgroup>
      <col width=65%>
      <col width=40%>
      <col width=60%>
      <col width=80%>
    </colgroup>
    <tr><th class="cell-meta-one" colspan="4">${117}</th></tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.festnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['festnetz_117'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_117_festnetz', lang)}</th>
        <td class="cell-meta">${_(fn_addresse_117)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.mobilnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['mobile_117'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_117_mobil', lang)}</th>
        <td class="cell-meta">${_(mo_addresse_117)|n}</td>
    </tr>
</table>
<tr><td class="cell-meta-one" colspan="2">&nbsp;</td></tr>
<table class="table-with-border">
    <colgroup>
      <col width=65%>
      <col width=40%>
      <col width=60%>
      <col width=80%>
    </colgroup>
    <tr><th class="cell-meta-one" colspan="4">${118}</th></tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.festnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['festnetz_118'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_118_festnetz', lang)}</th>
        <td class="cell-meta">${_(fn_addresse_118)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.mobilnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['mobile_118'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_118_mobil', lang)}</th>
        <td class="cell-meta">${_(mo_addresse_118)|n}</td>
    </tr>
</table>
<tr><td class="cell-meta-one" colspan="2">&nbsp;</td></tr>
<table class="table-with-border">
    <colgroup>
      <col width=65%>
      <col width=40%>
      <col width=60%>
      <col width=80%>
    </colgroup>
    <tr><th class="cell-meta-one" colspan="4">${143}</th></tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.festnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['festnetz_143'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_143_festnetz', lang)}</th>
        <td class="cell-meta">${_(fn_addresse_143)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.mobilnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['mobile_143'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_143_mobil', lang)}</th>
        <td class="cell-meta">${_(mo_addresse_143)|n}</td>
    </tr>
</table>
<tr><td class="cell-meta-one" colspan="2">&nbsp;</td></tr>
<table class="table-with-border">
    <colgroup>
      <col width=65%>
      <col width=40%>
      <col width=60%>
      <col width=80%>
    </colgroup>
    <tr><th class="cell-meta-one" colspan="4">${144}</th></tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.festnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['festnetz_144'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_144_festnetz', lang)}</th>
        <td class="cell-meta">${_(fn_addresse_144)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.mobilnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['mobile_144'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_144_mobil', lang)}</th>
        <td class="cell-meta">${_(mo_addresse_144)|n}</td>
    </tr>
    <tr>
</table>
<td class="cell-meta-one" colspan="2">&nbsp;</td></tr>
<table class="table-with-border">
    <colgroup>
      <col width=65%>
      <col width=40%>
      <col width=60%>
      <col width=80%>
    </colgroup>
    <tr><th class="cell-meta-one" colspan="4">${147}</th></tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.festnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['festnetz_147'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_147_festnetz', lang)}</th>
        <td class="cell-meta">${_(fn_addresse_147)|n}</td>
    </tr>
    <tr>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.mobilnetz', lang)}</th>
        <td class="cell-meta">${c['attributes']['mobile_147'] or '-'}</td>
        <th class="cell-meta">${t.Translator.translate('ch.bakom.notruf.adresse_147_mobil', lang)}</th>
        <td class="cell-meta">${_(mo_addresse_147)|n}}</td>
    </tr>
</table>
</%def>
