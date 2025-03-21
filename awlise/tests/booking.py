import asyncio
import os
import sys
from dotenv import load_dotenv

# Ensure the pyproject.toml file is valid or remove logfire dependency if unnecessary

# Add the project directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../awlise")))

from awlise.api.login import login_credentials
from awlise.api.getBooking import getBookings
load_dotenv()


site_id = os.getenv("ALISE_SITE_ID")
username = os.getenv("ALISE_USERNAME")
password = os.getenv("ALISE_PASSWORD")

def test_bookings():
    session = asyncio.run(login_credentials(site_id, username, password))
    bookings = asyncio.run(getBookings(session))
    return bookings

print(test_bookings()) # None