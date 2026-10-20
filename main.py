# this is wordle, created in python
# list of words from https://github.com/Blkzer0/Wordlists/blob/master/5-letters.txt

import time # used in intro
import random # used to pick random word from list

# stores all words from downloaded file in a list
with open("5-letters.txt", "r") as f:
    words = [line.strip() for line in f]

# colors
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[48;2;188;160;51m'
BG_BLACK = '\033[40m'
WHITE = '\033[97m'
GREEN = '\033[92m'
YELLOW  = '\033[93m'
GREY = '\033[90m'
RESET = '\033[0m' # returns to standard terminal text color

# js game instructions
def intro():
    print("welcome to WORDLE")
    time.sleep(2)
    print("alr basically")
    time.sleep(1)
    print("you get 6 chances to guess a 5 letter word")
    time.sleep(1)
    print(f"letters that are correct and in the right spot are {GREEN}green{RESET}")
    time.sleep(1)
    print(f"letters that are correct and in the wrong spot are {YELLOW}yellow{RESET}")
    time.sleep(1)
    print(f"letters that are incorrect are {GREY}gray{RESET}")

# used at start of game, returns true/false used in game loop
def play_first():
    user_response = input("you wanna play? (y/n) ")
    if user_response == "y" or user_response == "Y":
        return True
    elif user_response == "n" or user_response == "N":
        return False
    else: 
        print("pls enter valid response")
        play_first()

# used to repeat game, returns true/false used in game loop
def play_again():
    user_response = input("play again? (y/n) ")
    if user_response == "y" or user_response == "Y":
        return True
    elif user_response == "n" or user_response == "N":
        return False
    else: 
        print("pls enter valid response")
        play_again()
    
# takes in user's guess, while loop that goes on until no tries left
def user_guess():
    global word
    word = (random.choice(words)).upper()
    tries = 6
    while tries != -1:
        if tries == 0:
            return False
        word_guess = (input(f"\nu got {tries} tries left. give me a guess: " + word)).upper()
        if len(word_guess) != 5:
            print("boy enter a word with 5 letters")
            continue 
        if word_guess.lower() not in words:
            print("not in english word list.")
            continue
        win_or_lose = check_letters(word, word_guess)
        if win_or_lose == True:
            return True
        tries -= 1

    
# checks if user's letters correct by comparing w/ list of letters of real word
def check_letters(word, word_guess):
    real_word = []
    for letters in word:
        real_word.append(letters)

    user_letters = []
    for letter in word_guess:
        user_letters.append(letter)

    if word_guess == word:
        return True

    for i in range(0, len(user_letters)):
        if user_letters[i] == real_word[i]:
            print(BG_GREEN + WHITE + user_letters[i] + RESET, end="")
        elif user_letters[i] in real_word:
            print(BG_YELLOW + WHITE + user_letters[i] + RESET, end="")
        else:
            print(BG_BLACK + WHITE + user_letters[i] + RESET, end="")

# full game loop    
def game_loop(): 
    intro()
    lets_go = play_first()
    if lets_go:
        did_u_win = user_guess()
        if did_u_win == True:
            print("yoo you won")
        elif did_u_win == False: 
            print("damnnn you lost lmao!")
            time.sleep(1)
            global word
            print(f"btw the word was {word}")
        else:
            return
    else: 
        print("bru alr bye")
        return

    keep_playing = True
    while keep_playing == True:
        user_will = play_again()
        if user_will == False:
            keep_playing = False
            print("thanks for playing!")
        else: 
            did_u_win = user_guess()
            if did_u_win == True:
                print("yoo you won")
            elif did_u_win == False: 
                print("damnnn you lost lmao!")
                time.sleep(1)
                print(f"btw the word was {word}")
            else:
                return    
            
game_loop()
