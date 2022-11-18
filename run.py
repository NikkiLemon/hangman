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
SHEET = GSPREAD_CLIENT.open('hangman_words')

animals = SHEET.worksheet('animals')
fruits = SHEET.worksheet('fruits')
pixar_movies = SHEET.worksheet('pixar_movies')

animals_data = animals.get_all_values()

def get_random_word(animals_data):
    """
    This function returns a random words from the 
    Google sheet
    """
    animal_word = random.randint(1, len(animals_data) -1)
    return animals_data[animal_word]

print(get_random_word(animals_data))