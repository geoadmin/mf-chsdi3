<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        layer = c['layerBodId']
        lang = 'de' if lang in ('de', 'rm', 'en') else 'fr'
        sn_01_text = 'sn_01_%s' % lang
        nutz_01_text = 'nutz_01_%s' % lang
        schutz_01_text = 'schutz_01_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_(layer + '.sn_01')}</td>
        <td>${c['attributes'][sn_01_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.nutz_01')}</td>
        <td>${c['attributes'][nutz_01_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.schutz_01')}</td>
        <td>${c['attributes'][schutz_01_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.nutz_02')}</td>
        <td>${c['attributes']['nutz_02'] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
        def text_separation(arr_prot):
            arr = arr_prot.split(',')
            arr_len = len(arr)
            str_output = ''
            for i in range(arr_len):
                str_output = str_output + arr[i] + '<br />' if  i < (arr_len-1) else str_output + arr[i]
            endfor
            return str_output

        layer = c['layerBodId']
        lang = 'de' if lang in ('de', 'rm', 'en') else 'fr'
        sn_01_text = 'sn_01_%s' % lang
        nutz_01_text = 'nutz_01_%s' % lang
        schutz_01_text = 'schutz_01_%s' % lang
        pruefwert_text = 'pruefwert_%s' % lang
        nutz_05_text = 'nutz_05_%s' % lang
        nutz_08_text = 'nutz_08_%s' % lang
        nutz_09_text = 'nutz_09_%s' % lang
        prot_10_text = 'prot_10_%s' % lang
        prot_20_text = 'prot_20_%s' % lang
        prot_30_text = 'prot_30_%s' % lang
        prot_40_text = 'prot_40_%s' % lang
        prot_60_text = 'prot_60_%s' % lang
        prot_70_text = 'prot_70_%s' % lang

        prot_10_text = text_separation(prot_10_text)
        prot_20_text = text_separation(prot_20_text)
        prot_30_text = text_separation(prot_30_text)
        prot_40_text = text_separation(prot_40_text)
        prot_60_text = text_separation(prot_60_text)
        prot_70_text = text_separation(prot_70_text)
    %>

    <table class="table-with-border">
         <tr>
            <th colspan="2">${_(layer + '.solaranlagen_subtitle_1')}</th>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.sn_01')}</td>
            <td>${c['attributes'][sn_01_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_01')}</td>
            <td>${c['attributes'][nutz_01_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.schutz_01')}</td>
            <td>${c['attributes'][schutz_01_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.pruefwert')}</td>
            <td>${c['attributes'][pruefwert_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_02')}</td>
            <td>${c['attributes']['nutz_02'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_03')}</td>
            <td>${c['attributes']['nutz_03'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_04')}</td>
            <td>${c['attributes']['nutz_04'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_05')}</td>
            <td>${c['attributes'][nutz_05_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_06')}</td>
            <td>${c['attributes']['nutz_06'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_07')}</td>
            <td>${c['attributes']['nutz_07'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_08')}</td>
            <td>${c['attributes'][nutz_08_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_09')}</td>
            <td>${c['attributes'][nutz_09_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.nutz_10')}</td>
            <td>${c['attributes']['nutz_10'] or '-'}</td>
        </tr>
         <tr>
            <th colspan="2">${_(layer + '.solaranlagen_subtitle_2')}</th>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.prot_70')}</td>
            <td>${c['attributes'][prot_70_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.prot_60')}</td>
            <td>${c['attributes'][prot_60_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.prot_40')}</td>
            <td>${c['attributes'][prot_40_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.prot_30')}</td>
            <td>${c['attributes'][prot_30_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.prot_20')}</td>
            <td>${c['attributes'][prot_20_text] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(layer + '.prot_10')}</td>
            <td>${c['attributes'][prot_10_text] or '-'}</td>
        </tr>
    </table>
</%def>
