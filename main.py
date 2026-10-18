# this is wordle, created in python

def intro():
    print("welcome to WORDLE")
    print("play by blah blah blah")

def play_first():
    user_response = input("you wanna play? (y/n) ")
    if user_response == "y" or user_response == "Y":
        return True
    elif user_response == "n" or user_response == "N":
        return False
    else: 
        print("pls enter valid response")
        play_first()

def play_again():
    user_response = input("play again? (y/n) ")
    if user_response == "y" or user_response == "Y":
        return True
    elif user_response == "n" or user_response == "N":
        return False
    else: 
        print("pls enter valid response")
    

def user_guess():
    word = "AUDIO"
    tries = 6
    while tries != -1:
        if tries == 0:
            return False
        word_guess = input(f"u got {tries} tries left. give me a guess: ")
        win_or_lose = check_letters(word, word_guess)
        if win_or_lose == True:
            return True
        tries -= 1

    

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
            print(f"{user_letters[i]} is in the right spot")
        elif user_letters[i] in real_word:
            print(f"{user_letters[i]} is in the word but wrong spot")
        else:
            print(f"{user_letters[i]} is not in the word")

    
def game_loop():
    intro()
    lets_go = play_first()
    if lets_go:
        did_u_win = user_guess()
        if did_u_win == True:
            print("yoo you won")
        elif did_u_win == False: 
            print("damnnn you lost lmao!")
        else:
            return
    else: 
        print("bru alr bye")

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
            else:
                return    
            

game_loop()
