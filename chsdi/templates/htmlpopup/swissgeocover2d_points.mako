<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr',) else 'de'
    attrs = c['attributes']
    kind_label = attrs.get('kind_' + lang) or '-'
    spec = attrs.get('spec_' + lang) or '-'
    # Borehole-type kinds by integer code (10501001–10501004):
    # Bohrung, Sondierschlitz, Handsondierung, Rammsondierung
    BOREHOLE_KINDS = {10501001, 10501002, 10501003, 10501004}
    # Structural/orientation measurement kinds (azimuth + dip ± polarity)
    STRUCTURAL_KINDS = {
        13601001, 13601002, 13601003,
        13701001, 13701002, 13701004,
        13801001, 13801002, 13801003, 13801004, 13801005, 13801006,
        14601004,
    }
    is_bohrung = attrs.get('kind') in BOREHOLE_KINDS
    is_structural = attrs.get('kind') in STRUCTURAL_KINDS

    def fmt_num(val, sentinel=888):
        if val is None or val >= sentinel:
            return '-'
        if val == int(val):
            return str(int(val)) + ' m'
        return str(val) + ' m'

    def fmt_any(val):
        if val is None or val == '' or val == 0:
            return '-'
        if isinstance(val, float) and val == int(val):
            return str(int(val))
        return str(val)
%>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.kind')}</td>
        <td>${kind_label}</td>
    </tr>
    % if is_structural:
    <%
        _pol = attrs.get('mpla_polarity_' + lang) or ''
        polarity = '-' if not _pol or 'not applicable' in _pol or 'nicht anwendbar' in _pol else _pol
        azimuth_val = attrs.get('azimuth')
        dip_val = attrs.get('dip')
        azimuth_str = str(int(azimuth_val)) if azimuth_val is not None and azimuth_val < 999990 else '-'
        dip_str = str(int(dip_val)) if dip_val is not None and dip_val < 999990 else '-'
    %>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.mpla_polarity')}</td>
        <td>${polarity}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.dip_direction')}</td>
        <td>${azimuth_str}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.dip')}</td>
        <td>${dip_str}</td>
    </tr>
    % elif not is_bohrung:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.spec')}</td>
        <td>${spec}</td>
    </tr>
    % else:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_ref_number')}</td>
        <td>${fmt_any(attrs.get('abor_ref_number'))}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.azimuth')}</td>
        <td>${fmt_any(attrs.get('azimuth'))}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_depth_fm_a')}</td>
        <td>${fmt_num(attrs.get('abor_depth_fm_a'))}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_fm_a')}</td>
        <td>${attrs.get('abor_fm_a_' + lang) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_depth_fm_b')}</td>
        <td>${fmt_num(attrs.get('abor_depth_fm_b'))}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_fm_b')}</td>
        <td>${attrs.get('abor_fm_b_' + lang) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_depth_bedr')}</td>
        <td>${fmt_num(attrs.get('abor_depth_bedr'))}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_depth_tot')}</td>
        <td>${fmt_num(attrs.get('abor_depth_tot'), sentinel=999990)}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.abor_depth_wt')}</td>
        <td>${fmt_num(attrs.get('abor_depth_wt'), sentinel=999990)}</td>
    </tr>
    % endif
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.erl_link')}</td>
        <td>${h.pipe_links(attrs.get('erl_link')) | n}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.ber_link')}</td>
        <td>${h.pipe_links(attrs.get('ber_link')) | n}</td>
    </tr>
</%def>
