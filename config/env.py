import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class UserData(object):
    Browser = os.getenv("BROWSER")
    Headless = os.getenv("HEADLESS") == 'yes'
    ValidEmail = os.getenv("EMAIL")
    ValidPassword = os.getenv("PASSWORD")
    BaseURL = os.getenv("URL")
    Timeout = os.getenv("TIMEOUT")
    InvalidEmail = ("NotMyEmail")
    UnregisteredEmail = ("NotRegisteredYet@sharklasers.net")
    InvalidPassword = ("ABC123abc")