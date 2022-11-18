import random
import gspread
from google.oauth2.service_account import Credentials
from hangman import display_hangman

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
    animal_word = random.randint(0, len(animals_data) - 1)
    return animals_data[animal_word]

def display_board(missed_letters, correct_letters, secret_word):
    print(display_hangman[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        """
        Replace blanks with correctly guessed letters
        """
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks [i:1]
    
    for letter in blanks:
        """
        Show the secret word with spaces in between each letter
        """
        print(letter, end=' ')
    print()


def main():
    print(get_random_word(animals_data))
    print('H A N G M A N')
    missed_letters = ' '
    correct_letters = ' '
    secret_word = get_random_word(animals_data)
    display_board(missed_letters, correct_letters, secret_word)
main()