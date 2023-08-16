<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
    bez_text = 'bez_%s' % lang
%>

<tr>
  <td class="cell-left">${_('ch.blw.milchmarktregionen.milchreg')}</td>
  <td class="cell-left">${c['attributes'][bez_text] or '-' }</td>
</tr>

</%def>
