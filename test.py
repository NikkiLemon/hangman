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

words = SHEET.worksheet('words')
fruits = SHEET.worksheet('fruits')
pixar_movies = SHEET.worksheet('pixar_movies')

words_data = words.get_all_values()



def get_random_word(words_data):
    """
    This function returns a random words from the 
    Google sheet
    """
    word = random.choice(words_data)
    print(word)
    return word 


def hide_word(words_data):
    """
    Change the game word into underscores(_)
    ready for the player to guess
    """
    word_split = list(word).split

    hidden_word = []

    for letter in word_split:
        letter = "_"
        hidden_word.append(letter)
    
    hidden_game_word = ""

    for letter in hidden_word:
        hidden_game_word += letter

    print(hidden_game_word)














def main():
    get_random_word(words_data)
    hide_word(get_random_word)

main()
