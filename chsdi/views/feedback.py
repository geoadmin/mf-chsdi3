# -*- coding: utf-8 -*-

import cgi
import json
import datetime
from pyramid.view import view_config

from pyramid.httpexceptions import HTTPInternalServerError
from smtplib import SMTPException


# http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html
@view_config(route_name='feedback', renderer='json', request_method='POST')
def feedback(context, request):
    defaultRecipient = 'webgis@swisstopo.ch'
    defaultSubject = 'Customer feedback'

    def getParam(param, defaultValue):
        val = request.params.get(param, defaultValue)
        val = val if val != '' else defaultValue
        return val

    def mail(to, subject, text, attachement, kml, kmlfilename, jsonToAttach):
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEBase import MIMEBase
        from email.MIMEText import MIMEText
        from email import Encoders
        import unicodedata
        import smtplib

        msg = MIMEMultipart()

        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(
            MIMEText(unicodedata.normalize('NFKD',
                                           unicode(text)).encode('UTF-8',
                                                                 'ignore'),
                     _charset='utf-8'))
        # Attach meta information
        part = MIMEBase('application', 'json')
        part.set_payload(json.dumps(jsonToAttach))
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=' + jsonfilename)
        msg.attach(part)

        # Attach file if there
        if isinstance(attachement, cgi.FieldStorage):
            types = attachement.type.split('/')
            if len(types) != 2:
                raise HTTPInternalServerError('File type could not be determined')
            part = MIMEBase(types[0], types[1])
            filePart = attachement.file.read()
            part.set_payload(filePart)
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % attachement.filename)
            msg.attach(part)

        # Attach kml if there
        if kml is not None and kml is not '':
            part = MIMEBase('application', 'vnd.google-earth.kml+xml')
            kml = kml.encode('UTF-8')
            part.set_payload(kml)
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename=' + kmlfilename)
            msg.attach(part)

        mailServer = smtplib.SMTP('127.0.0.1', 25)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        # Recipients and sender are always the same
        mailServer.sendmail(to, to, msg.as_string())
        mailServer.close()

    ua = getParam('ua', 'no user-agent found')
    permalink = getParam('permalink', 'No permalink provided')
    feedback = getParam('feedback', 'No feedback provided')
    email = getParam('email', 'Anonymous')
    version = getParam('version', 'No version provided')
    text = u'%s sent a feedback:\n %s.\n\nPermalink: %s.\n\nUser-Agent: %s\n\nApplication Version: %s'
    attachement = getParam('attachement', None)
    kml = getParam('kml', None)
    now = datetime.datetime.now()
    timeID = now.strftime('%Y%m%d%H%M%S%f')[0:16]
    defaultSubject = defaultSubject + ' ID : ' + timeID
    kmlfilename = 'Drawing-' + timeID + '.kml'
    jsonfilename = 'Meta-' + timeID + '.json'
    attachfilename = ''
    if isinstance(attachement, cgi.FieldStorage):
        attachfilename = attachement.filename

    jsonAtt = {
        'emailAddress': email,
        'body': feedback,
        'permalink': permalink,
        'kml': kmlfilename if (kml is not None and kml is not '') else '',
        'attachement': attachfilename,
        'userAgent': ua,
        'ID': timeID
    }

    try:
        mail(
            defaultRecipient,
            defaultSubject,
            text % (email, feedback, permalink, ua, version),
            attachement,
            kml,
            kmlfilename,
            jsonAtt
        )
    except SMTPException:
        raise HTTPInternalServerError()

    return {'success': True}
