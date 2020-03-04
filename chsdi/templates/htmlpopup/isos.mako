# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%!
   from chsdi.lib.helpers import quoting
%>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('kanton', lang)}</td>                     <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ortsbildname', lang)}</td>               <td>${c['attributes']['ortsbildname']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('kategorie', lang)}</td>                  <td>${c['attributes']['vergleichsrastereinheit'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('lagequalitaeten', lang)}</td>            <td>${c['attributes']['lagequalitaeten'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('raeumliche_qualitaeten', lang)}</td>     <td>${c['attributes']['raeumliche_qualitaeten'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('arch__hist__qualitaeten', lang)}</td>    <td>${c['attributes']['arch__hist__qualitaeten'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('fassung', lang)}</td>                    <td>${c['attributes']['fassungsjahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('band_1_2', lang)}</td>                   <td>${c['attributes']['band_1'] or '-'} | ${c['attributes']['band_2'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('publikationsjahr_1_2', lang)}</td>       <td>${c['attributes']['publikationsjahr_1'] or '-'} | ${c['attributes']['publikationsjahr_2'] or '-'}</td></tr>
<%
dataHost = request.registry.settings['datageoadminhost']
dataPath = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder/PDF'
url_pdf = None
url_pdf2 = None
if c['attributes']['pdf_dokument_1']:
  url_pdf = '//%s/%s/%s.pdf' % (dataHost, dataPath, c['attributes']['pdf_dokument_1'])
if c['attributes']['pdf_dokument_2']:
  url_pdf2 = '//%s/%s/%s.pdf' % (dataHost, dataPath, c['attributes']['pdf_dokument_2'])

pdfname = []
if c['attributes']['pdfspecial'] is not None:
    pdfname = c['attributes']['pdfspecial'].split(',')
%>
    <tr>
      % if  c['attributes']['pdf_dokument_1'] != 'ISOS_5800':
      <td class="cell-left">${mod_translate.Translator.translate('pdf_dokument_1_2', lang)}</td>
      <td>
        % if c['attributes']['pdf_dokument_1']:
            <a href="${url_pdf}" target="_blank">${c['attributes']['pdf_dokument_1']}.pdf</a> |
        % else:
            - | 
        % endif
        % if c['attributes']['pdf_dokument_2']:
            &nbsp;<a href="${url_pdf2}" target="_blank">${c['attributes']['pdf_dokument_2']}.pdf</a>
        % else:
            &nbsp;-
        % endif
      </td>
      % elif c['attributes']['pdf_dokument_1'] == 'ISOS_5800' :
      <td class="cell-left" style="vertical-align: top;">PDFs</td>
      <td>
          % for name in pdfname:
          <a href="//${dataHost}/${dataPath}/ISOS_5800_${name}.pdf"  target="_blank">ISOS_5800_${name}.pdf<a/><br>
          % endfor
      </td>
      % endif
    </tr>
    <tr><td colspan=2>${mod_translate.Translator.translate('ch.bak.isos.warning', lang)}</td></td></tr>
</%def>
