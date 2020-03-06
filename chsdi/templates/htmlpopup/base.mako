# -*- coding: utf-8 -*-

<%!
  from pyramid.url import route_url
  import chsdi.lib.helpers as h

%>
<%
  lang = request.lang
  topic = request.matchdict.get('map')
  c['stable_id'] = False
  hasExtendedInfo = c.get('hasExtendedInfo')
  isExtended = c.get('isExtended')
  isIframe = c.get('isIframe')
  isGridLayer = c.get('isGridLayer')
  c['htmlpopup_class'] = c['layerBodId'].replace('.', '')
  timestamp = c.get('time')
 %>

% if isExtended or isIframe:
<head>
  <!--[if !HTML5]>
  <meta http-equiv="X-UA-Compatible" content="IE=9,IE=10,IE=edge,chrome=1"/>
  <![endif]-->
  <title>${c['fullName']}</title>
  <meta name="viewport" content="initial-scale=1.0"/>
  <link rel="shortcut icon" type="image/x-icon" href="${h.versioned(request.static_url('chsdi:static/images/favicon.ico'))}">
  <link rel="apple-touch-icon" sizes="76x76" href="${h.versioned(request.static_url('chsdi:static/images/touch-icon-bund-76x76.png'))}"/>
  <link rel="apple-touch-icon" sizes="120x120" href="${h.versioned(request.static_url('chsdi:static/images/touch-icon-bund-120x120.png'))}"/>
  <link rel="apple-touch-icon" sizes="152x152" href="${h.versioned(request.static_url('chsdi:static/images/touch-icon-bund-152x152.png'))}"/>
  <link rel="stylesheet" type="text/css" href="${h.versioned(request.static_url('chsdi:static/css/extended.min.css'))}"/>
  % if hasattr(self, 'extended_resources'):
    ${self.extended_resources(c, lang)}
  % endif
</head>
% endif

% if isExtended:
<body>
  <div class="chsdi-htmlpopup-container">
% else:
  <div id="${c['layerBodId']}#${c['featureId']}" class="${c['htmlpopup_class']} htmlpopup-container">
% endif

% if not isIframe:
  <div class="htmlpopup-header">
    <span>${c['fullName']}</span> (${c['attribution']})
  </div>
% endif

  <div class="htmlpopup-content">
    % if isExtended:
      ${self.extended_info(c, lang)}
    % elif isIframe:
      % if hasattr(self, 'iframe_content'):
        ${self.iframe_content(c, lang)}
      % endif
    % else:
      <table>
        ${self.table_body(c, lang)}
        % if hasExtendedInfo:
        <tr>
          % if isGridLayer:
            <td colspan="2">
          % else:
            <td class="cell-left"></td>
            <td>
          % endif
              <a href="${h.make_agnostic(request.route_url('extendedHtmlPopup', map=topic, layerId=c['layerBodId'], featureId=str(c['featureId'])))}?lang=${lang}" target="_blank">
                ${h.translate('zusatzinfo', lang)}&nbsp;<img src="${h.versioned(request.static_url('chsdi:static/images/ico_extern.gif'))}" />
              </a>
            </td>
        </tr>
        % endif
        % if c['stable_id'] is True:
          <tr>
          % if isGridLayer:
            <td colspan="2">
          % else:
            <td class="cell-left"></td>
            <td>
          % endif
              <a href="${''.join((c['baseUrl'], '?', c['layerBodId'], '=', str(c['featureId']), '&time={}'.format(timestamp), '&lang=', lang, '&topic=', topic))}" target="new">
                ${h.translate('Link to object', lang)}
              </a>
            </td>
          </tr>
        %endif
      </table>
    % endif
  </div>
  % if isExtended:
  <div class="htmlpopup-footer">
    <a href="${h.translate('disclaimer url', lang)}" target="_blank">
      ${h.translate('disclaimer title', lang)}
    </a>
    <div class="float-right">
      % if c['stable_id'] is True:
      <a class="link" href="${''.join((c['baseUrl'], '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic))}" target="new">
        ${h.translate('Link to object', lang)}
      </a>
      &nbsp;|&nbsp;
      % endif
      <a href="javascript:window.print();">
        ${h.translate('print', lang)}
      </a>
    </div>
    </div>
  </div>
  % endif
</div>
% if isExtended:
</body>
% endif
