import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fortune_teller')


def welcome_message():
    """
    Welcome message
    """
    print("Welcome child to the Best Fortune Teller!")
    print("You can ask me everything you want")
    print("...but if you want better results,")
    print("I advice you to ask questions with Yes or No responses")


welcome_message()