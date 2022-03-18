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

    # Ask user name
    print("Let's start with your name")

    name = input ("Please type your name here:")
    print(f"So {name} what do you want to know?")

    # Ask user question
    question = input("Please type your question here:")
    print (f"So you ask this '{question}'.")
    print ("Let me see what me eight ball says...")
    print("ups...I mean...my crystal Ball.")

    # Ask if user wants to continue or leave
    print (f" {name} Do you want to ask me anything else?")
    
    anotherQuestion = input("Please type Yes or No here: ")

    if anotherQuestion != "Yes":
        print(f"Bye {name}")
        quit()
    
    print("Okay! What do you want to know now?")



welcome_message()