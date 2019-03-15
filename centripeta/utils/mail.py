#!/usr/bin/python3
from email.message import EmailMessage
from smtplib import SMTP

def send_email(subject, body, mail_to, mail_from, smtp_server, smtp_port, smtp_user, smtp_pass, tls=False):
    """Simple function to send e-mail notifications with Python smtplib
    
    Arguments:
        subject {str} -- Message subject
        body {str} -- Message body
        mail_to {str} -- Recipient address. Multiple addresses separated by comma also work
        mail_from {str} -- Sender address
        smtp_server {str} -- SMTP server address/name
        smtp_port {str} -- SMTP port (defaults to 25).
        smtp_user {str} -- Username, if SMTP server requires authentication
        smtp_pass {str} -- Password, if SMTP server requires authentication
    
    Keyword Arguments:
        tls {bool} -- Whether to use TLS connection with STARTTLS method (default: {False})
    """
    # Create email message & fuck sanity checks
    msg = EmailMessage()
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg["Subject"] = subject
    msg.set_content(body)

    # Send message
    server = SMTP(smtp_server, smtp_port)
    if tls is True:
        server.starttls()
    if smtp_user != "":
        server.login(smtp_user, smtp_pass)
    server.sendmail(mail_from, mail_to, msg.as_string())
    server.quit() 

def make_mailer(default_mail_to, default_mail_from="croningp-platforms@chem.gla.ac.uk", default_smtp_server="smtp.chem.gla.ac.uk", default_smtp_port="25", default_smtp_user="", default_smtp_pass="", use_tls=False):
    """Simple factory to create send_email() instances with default arguments set"""
    def wrapper(subject, body):
        send_email(subject, body, mail_to=default_mail_to, mail_from=default_mail_from, smtp_server=default_smtp_server, smtp_port=default_smtp_port, smtp_user=default_smtp_user, smtp_pass=default_smtp_pass, tls=use_tls)
    return wrapper
