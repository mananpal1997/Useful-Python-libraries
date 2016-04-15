from envelopes import Envelope, GMailSMTP

envelope = Envelope(
    from_addr=(u'sender@abc.com', u'From Sender'),
    to_addr=(u'receiver@xyz.com', u'To Receiver'),
    subject=u'Envelopes demo',
    text_body=u"Hello, world!"
)
#attach anything
#envelope.add_attachment('abc.jpg')
envelope.send('smtp.googlemail.com', login='sender@abc.com',password='password', tls=True)
#OR
'''
gmail = GMailSMTP('sender@abc.com', 'password')
gmail.send(envelope)
'''
