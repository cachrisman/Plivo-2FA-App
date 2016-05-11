# settings.py contains all the global settings / configurations
# for the application.
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# Application Title
SITE_TITLE = "Plivo 2FA"

# Application mode
DEBUG = True

# Redis URI
APPLICATION_REDIS_URI = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# Plivo Configurations
PLIVO_AUTH_ID = os.environ.get('PLIVO_AUTH_ID')
PLIVO_AUTH_TOKEN = os.environ.get('PLIVO_AUTH_TOKEN')
PLIVO_NUMBER = os.environ.get('PLIVO_NUMBER', '')

# The MESSAGE_TEXT should be less than 160 characters and contain
# a `__code__` string which will be replaced by the code generated
# before sending the SMS
MESSAGE_TEXT = "Your verification code is __code__"

# Verification codes will be valid for CODE_VALIDITY number of seconds
CODE_VALIDITY = 15*60