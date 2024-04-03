<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.solarenergie-einstrahlung_0_grad.Ausrichtung')}</td>    
    <td>${_('Ausrichtung')}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.solarenergie-einstrahlung_0_grad.Neigung_Einstrahlungsebene')}</td>    
    <td>${_('Neigung_Einstrahlungsebene_0_grad')}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_jahressumme_kwhm2')}</td>    
    <td>${c['attributes']['globalstrahlung_jahressumme_kwhm2'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_wintersumme_kwhm2')}</td>
    <td>${c['attributes']['globalstrahlung_wintersumme_kwhm2'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_jahressumme_kwhkwp')}</td>    
    <td>${c['attributes']['pvproduktion_jahressumme_kwhkwp'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_wintersumme_kwhkwp')}</td>
    <td>${c['attributes']['pvproduktion_wintersumme_kwhkwp'] or '-'}</td>
  </tr>
</%def>

<%def name="extended_info(c, lang)">
  <table>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.Ausrichtung')}</td>    
      <td class="cell-meta">${_('Ausrichtung')}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.Neigung_Einstrahlungsebene')}</td>    
      <td class="cell-meta">${_('Neigung_Einstrahlungsebene_0_grad')}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.Koordinaten')}</td>    
      <td class="cell-meta">${c['attributes']['x'] or '-'},${c['attributes']['y'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_jahressumme_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_jahressumme_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_wintersumme_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_wintersumme_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_januar_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_januar_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_februar_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_februar_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_maerz_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_maerz_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_april_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_april_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_mai_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_mai_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_juni_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_juni_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_juli_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_juli_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_august_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_august_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_september_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_september_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_oktober_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_oktober_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_november_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_november_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.globalstrahlung_dezember_kwhm2')}</th>
      <td class="cell-meta">${c['attributes']['globalstrahlung_dezember_kwhm2'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_jahressumme_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_jahressumme_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_wintersumme_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_wintersumme_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_januar_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_januar_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_februar_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_februar_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_maerz_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_maerz_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_april_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_april_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_mai_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_mai_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_juni_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_juni_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_juli_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_juli_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_august_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_august_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_september_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_september_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_oktober_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_oktober_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_november_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_november_kwhkwp'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-meta">${_('ch.bfe.solarenergie-einstrahlung_0_grad.pvproduktion_dezember_kwhkwp')}</th>
      <td class="cell-meta">${c['attributes']['pvproduktion_dezember_kwhkwp'] or '-'}</td>
    </tr>
  </table>
</%def>

