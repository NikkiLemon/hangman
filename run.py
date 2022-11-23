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

word = SHEET.worksheet('words')
fruits = SHEET.worksheet('fruits')
pixar_movies = SHEET.worksheet('pixar_movies')

words_data = word.get_all_values()

chosen_word = ""

def get_word():
    chosen_word = random.choice(words_data)
    return chosen_word[0]

def play(chosen_word):
    word_completion = "-" * len(chosen_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        print(guessed_letters)

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in chosen_word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
            print(f"You have {tries} tries remaining")
            
        elif len(guess) == len(chosen_word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != chosen_word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = chosen_word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was ")
        print(chosen_word)
        print("Try again next time")

def play_again():
    while input("Play Again? (Y/N) ").upper() == "Y":
        chosen_word = get_word()
        play(chosen_word)


def main():
    chosen_word = get_word()
    play(chosen_word)
    play_again()


if __name__ == "__main__":
    main()
