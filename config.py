"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

from datetime import datetime
import tempfile

# file settings
LOG_FILENAME        = tempfile.gettempdir()+'/py3mailer.log'
CSV_RETRY_FILENAME  = tempfile.gettempdir()+'/py3mailer.csv'
STATS_FILE          = tempfile.gettempdir()+'/py3mailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# smtp settings
SMTP_HOST     = ''
SMTP_PORT     = '587'
SMTP_USER     = '' # Leave empty if not needed
SMTP_PASSWORD = '' # Leave empty if not needed
ENCRYPT_MODE  = 'starttls' # Choose between 'none', 'ssl' and 'starttls'

# the address and name the email comes from
FROM_NAME = 'Test Mail'
FROM_EMAIL = 'xy@mailxy.com'

# The number of emails to send to each recipient
NB_EMAILS_PER_RECIPIENT = 1

# test recipients list
TEST_RECIPIENTS = [
    {'VName': 'Name', 'test1_RECIPIENTS@mailxy.com': 'test1_RECIPIENTS@mailxy.com'},
]
