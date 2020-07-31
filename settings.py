from dotenv import load_dotenv
import os

#explicitly providing path to '.env'. Project folder should have .env file with mail_username and mail_password variables.
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
