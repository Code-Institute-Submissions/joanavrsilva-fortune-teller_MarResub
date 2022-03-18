"""
Import random for answers and google sheet with the answers
"""
import random
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


def fortune_teller():
    """
    Welcome message
    """
    print("Welcome child to the Best Fortune Teller!\n")
    print("You can ask me everything you want")
    print("...but if you want better results,")
    print("I advice you to ask questions with Yes or No responses\n")

    # Ask user name
    print("Let's start with your name")

    name = input("Please type your name: \n")
    print(f"So {name} what do you want to know?")

    # Ask user question
    question = input("Please type your question: \n")
    print(f"So you ask this '{question}'.")
    print("Let me see what my magic eight ball says...")
    print("ups...I mean...my crystal ball. \n")
    print("The awnswer is...")

    # Give user an answer
    all_magic_ball_answers = SHEET.worksheet('allMagicBallAnswers')

    answer_given = all_magic_ball_answers.col_values(1)

    print(random.choice(answer_given))

    # Ask if user wants to continue or leave
    print(f" {name} Do you want to ask me anything else?")

    another_question = input("Please type Yes or No: \n")

    if another_question.lower() != "yes":
        print(f"Bye {name} come back anytime!")
        quit()

    elif another_question.lower() == "yes":
        print("Okay! What do you want to know now?")
        new_question = input("Please type your new question:\n ")
        print(f"So you ask this '{new_question}'.")
        print("Let me see what my magic eight ball says...")
        print("ups...I mean...my crystal ball. \n")
        print("The awnswer is...")

        all_magic_ball_answers = SHEET.worksheet('allMagicBallAnswers')

        answer_given = all_magic_ball_answers.col_values(1)

        print(random.choice(answer_given))

        print(f" {name} I hope I was able to answer some of your questions!")
        print("Bye! See you next time!")
        quit()


fortune_teller()
