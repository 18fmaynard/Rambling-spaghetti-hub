from itertools import filterfalse
import random
words = []
letters_in_word = []
game_board =[]
def game(final_word):
    word_formatted = final_word.replace("\n","")
    word_length = len(word_formatted)
    for i in range(0,word_length):
        letters_in_word.append(word_formatted[i])
        game_board.append("_ ")
    print(game_board)
    playing(word_length, game_board)
        
def playing(word_length, gameboard):
    lives_left = True
    lives = 6
    while lives_left == True:
        print("You have ", lives, " lives remaining.")
        correct_input = False
        while correct_input == False:
            guess = input("What is your guess? ")
            if len(guess) == 1:
                if guess.isalpha() == True:
                    correct_input = True
                else:
                    correct_input = False
            else:
                correct_input = False
        guess_formatted = guess.upper()
        for i in range(0, word_length):
            if guess == letters_in_word[i]:
                game_board[i] = guess
        print(gameboard)
         
        
        
def select_word():
    Word_list = open("Classwork/Hangman/Word_list.txt","r")
    for i in range(1,98):
        Word_list_number = Word_list.readline()
        words.append(Word_list_number)
    final_word = words[random.randint(0,len(words))]
    game(final_word)
    Word_list.close()
        

def start():
    print("""

███████████████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─██─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀███─▄▄▄▄█─▄▄▄─█▄─▄█▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▄─▄▄─█
█─███▀█─██─██─█▄█─███─▄▄▄██─██─████─████─▄█▀██─▄─▄███▄▄▄▄─█─███▀██─███─▄█▀██─█▄▀─██─███▀██─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀  
                     _                                             
                    | |                                            
                    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                    | | | | (_| | | | | (_| | | | | | | (_| | | | |
                    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                        __/ |                      
                                       |___/                       
                                       _______
                                      |/      |
                                      |      (_)
                                      |      \|/
                                      |       |
                                      |      | |
                                      |
                                     _|___
          """)
    start_condition = input("                               Are you ready to play? ")
    
    if start_condition.upper() == "YES":
        select_word()
    else:
        start()
    
start()
