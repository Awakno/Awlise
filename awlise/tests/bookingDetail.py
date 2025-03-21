import asyncio
import datetime
import os
import sys
from dotenv import load_dotenv
# Ensure the pyproject.toml file is valid or remove logfire dependency if unnecessary

# Add the project directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../awlise")))

from awlise.api.login import login_credentials
from awlise.api.getBookingDetail import getBookingsDetail, getBookingDetailByDateISO8601
load_dotenv()


site_id = os.getenv("ALISE_SITE_ID")
username = os.getenv("ALISE_USERNAME")
password = os.getenv("ALISE_PASSWORD")

def test_bookings_by_iso():
    session = asyncio.run(login_credentials(site_id, username, password))
    bookings = asyncio.run(getBookingDetailByDateISO8601(session, datetime.datetime.now().isoformat().split("T")[0]))
    return bookings

print(test_bookings_by_iso()) # None