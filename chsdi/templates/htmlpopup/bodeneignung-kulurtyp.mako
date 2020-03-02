# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  Key_To_Translate = 'blw_farbe_' + str(c['attributes']['farbe'])
%>
  <tr>
    <td colspan="3">&nbsp;</td>
  </tr>
  <tr>
    <td width="30" bgcolor="${c['attributes']['symb_color']}" style="border-style: solid; border-width: 1px; -webkit-print-color-adjust:exact;">&nbsp;</td>
    <td width="20">&nbsp;</td>
    <td>${t.Translator.translate(Key_To_Translate, lang)}</td>
  </tr>
  <tr>
    <td>${t.Translator.translate('bodeneignung_id', lang)}</td>
    <td>&nbsp;</td>
    <td>${c['attributes']['farbe'] or '-'}</td>
  </tr>
  <tr>
    <td colspan="3">&nbsp;</td>
  </tr>
</%def>
