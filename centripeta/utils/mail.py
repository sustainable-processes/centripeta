import sendgrid
import os

class Notifier:
    ''' Class for sending notifications about notebooks/scripts
    
    Attributes
    ---------- 
    email: `str`
         Email neeed for sending keys
    key: `str``
        Sendgrid API key. By default this will be pulled from the environmental
        variable SENGRID_API_KEY
    Example
    -------
    from sre_tools import Notifier
    from time import sleep
    n = Notifier(email='joe@none.com')
    delay = 60
    time.sleep(delay)
    n.notification(subject=f'Email sent after {delay} seconds.')
    ''' 
    def __init__(self, email, key=None):
        self.sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENGRID_API_KEY', key))
        self._email = email
        self._check_valid_email(self._email)

    def notification(self, subject=None):
        ''' Send a notification 
        
        Parameters
        ---------- 
        subject: `str` (optional)
            Subject of the email. If left blank will default "Your job is complete."
        ''' 
        # TO:DO Replace with something like noreply@sre.ceb.cam.ac.uk
        from_email = Email("noreply@sre.ceb.cam.ac.uk")
        to_email = Email(self.email)
        if subject:
            pass
        else:
            subject = "Your job is complete"
        content = Content("text/plain", "Please see hub.cam.ac.uk for more information")
        mail = Mail(from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())

    def _check_valid_email(self, email):
        ''' Check if a string is formatted as an email'''
        m = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
        if m.group(0):
            return
        else:
            raise ValueError("Please pass a valid email")

    @property
    def email(self):
        '''Return the email being used by notifier'''
        return self._email

    @email.setter
    def email(self, email):
        '''Set the email being used by notifier'''
        self._check_valid_email(email)
        self._email = email