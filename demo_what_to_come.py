import random
import string
# === SECTIUNEA CONFIGURARE
MENUPICS_SELECT_SCREEN = 0
MENUPICS_EASY_DIFICULTY_SCREEN = 1
MENUPICS_HARD_DIFICULTY_SCREEN = 2
MENUPICS_HARD_DIFICULTY_SCREEN = 3


MENUPICS = [
    """
===================================================
||                                                 ||
||             Select your difficulty              ||
||                                                 ||
||                    1. EASY                      ||
||                   (8 Lives)                     ||
||             (less then 10 letters)              ||
||                                                 ||
||                    2. HARD                      ||
||                   (8 Lives)                     ||
||         (words with more then 10 letters        ||
||                                                 ||
 ===================================================
""",
    """
 ===================================================
||                                                 ||
||                                                 ||
||                                                 ||
||       Easy difficulty has been chosen.          ||
||              You have 8 lives.                  ||
||        Words with less then 10 letters          ||
||                                                 ||
||                                                 ||
 ===================================================
""",
    """
 ===================================================
||                                                 ||
||                                                 ||
||                                                 ||
||       Easy difficulty has been chosen.          ||
||              You have 8 lives.                  ||
||        Words with less then 10 letters          ||
||                                                 ||
||                                                 ||
 ===================================================
""",
    """
 ===================================================
||                                                 ||
||                                                 ||
||         Hard difficulty has been chosen.        ||
||                You have 8 lives                 ||
||         Words with more then 10 letters         ||
||                                                 ||
||                                                 ||
 ===================================================
"""
]


HANGMANPICS = ["""

 //++++++++++++++\\\\                           
 |#|                                                   _____                ___ ___              ___
 |#|                                                  / ____|               | | | |              | |   
 |#|                                                 | |  __  ___   ___   __| | | |    _   _  ___| | __
 |#|                                                 | | |_ |/ _ \ / _ \ / _` | | |   | | | |/ __| |/ /
 |#|                                                 | |__| | (_) | (_) | (_| | | |___| |_| | (__|   < 
 |#|                                                  \_____|\___/ \___/ \__,_| |______\__,_|\___|_|\_\\                              
 |#|
 |#|=============> """, """
 
 //++++++++++++++\\\\
 |#|      |          
 |#|          
 |#|     
 |#|                   
 |#|       
 |#|
 |#|
 |#|=============>""", """
 
 //++++++++++++++\\\\
 |#|      |
 |#|      O     
 |#|     
 |#|          
 |#|     
 |#|
 |#|
 |#|=============>""", """

 //++++++++++++++\\\\
 |#|      |
 |#|      O     
 |#|      |
 |#|          
 |#|       
 |#|
 |#|
 |#|=============>""", """
 
 //++++++++++++++\\\\
 |#|      |
 |#|      O     
 |#|      |
 |#|      |     
 |#|        
 |#|
 |#|
 |#|=============>""", """
 
 //++++++++++++++\\\\
 |#|      |
 |#|      O     
 |#|     /|
 |#|      |     
 |#|       
 |#|
 |#|
 |#|=============>""", """
 
 //++++++++++++++\\\\
 |#|      |
 |#|      O     
 |#|     /|\\
 |#|      |     
 |#|       
 |#|
 |#|
 |#|=============>""", """
 
 //++++++++++++++\\\\ 
 |#|      |
 |#|      O     
 |#|     /|\\
 |#|      |     
 |#|     /   
 |#|
 |#|
 |#|=============>""", """
 
 //++++++++++++++\\\\
 |#|      |
 |#|      O     
 |#|     /|\\
 |#|      |     
 |#|     / \\   
 |#| 
 |#| 
 |#|=============>"""]


# === SECTIUNEA DEFINIRE FUNCTII

def get_difficulty():
    print("""
    ===================================================
    ||                                                 ||
    ||             Select your difficulty              ||
    ||                                                 ||
    ||                    1. EASY                      ||
    ||                   (8 Lives)                     ||
    ||             (less then 10 letters)              ||
    ||                                                 ||
    ||                    2. HARD                      ||
    ||                   (8 Lives)                     ||
    ||         (words with more then 10 letters        ||
    ||                                                 ||
    ===================================================
    """)

    difficulty = input("Choose wisely!:")
    while difficulty not in ['1', '2']:
        print("Please input a valid option.")
        difficulty = input("Choose wisely!:")

    return difficulty


def get_word_to_be_guessed(difficulty):
    capitals = []
    countries = []
    if int(difficulty) < 2:
      return 'Sibiu'
    else:
      return 'Zimbabwe'


def get_lives(difficulty):
    if int(difficulty) == 1:
        return 8
    elif int(difficulty) == 2:
        return 8


def display_game_statistics(HANGMANPICS, missedLetters, correctLetters, word):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = "_"*len(word)

    for i in range(len(word)):
        if word[i] in correctLetters:
            blanks = blanks[:i] + word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(alreadyGuessed):

    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in string.ascii_lowercase:
            print("Please enter a LETTER")
        else:
            return guess


def playAgain():

    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')


def is_game_done(word, correctLetters):
    foundAllLetters = True
    for letter in word:
        if letter not in correctLetters:
            foundAllLetters = False
            break
    return foundAllLetters


def play(word, lives):
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False
    livesReset = lives
    while True:
        display_game_statistics(
            HANGMANPICS, missedLetters, correctLetters, word)

        guess = get_guess(missedLetters + correctLetters)

        if guess in word:
            correctLetters = correctLetters + guess
            if is_game_done(word, correctLetters):
                print("Yes, the correc word is ", word, " you have won")
                break

        else:
            missedLetters = missedLetters + guess
            lives = lives - 1

            if lives == 0:
                print("You have run out of lives!\nAfter ", str(livesReset), "missed guesses and ", str(
                    len(correctLetters)), " correct guesses, the word was ", "'", word, "'")
                gameIsDone = True
            else:

                print("Tries left: {0}".format(lives))

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    lives = livesReset
                    gameIsDone = False
                    word = get_word_to_be_guessed(difficulty)
                else:
                    break


difficulty = get_difficulty()
word = get_word_to_be_guessed(difficulty)
lives = get_lives(difficulty)
print(type(lives))
print("Tries left: {0}".format(lives))
play('word', lives)
