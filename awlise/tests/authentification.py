import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the project directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../awlise")))

from awlise.api.login import login_credentials
from awlise.api.home import home
load_dotenv()
username = os.getenv("ALISE_USERNAME")
password = os.getenv("ALISE_PASSWORD")
site_id = os.getenv("ALISE_SITE_ID")


def test_login():
    session = asyncio.run(login_credentials(site_id, username, password))
    return session

print(test_login()) # None

def test_home():
    session = test_login()
    home_data = asyncio.run(home(session))
    return home_data

print(test_home()) # None