import random
words = []
letters_in_word = []
game_board =[]
incorect = []

        

    



def playing(word_length, letters_in_word):
    lives_left = True
    lives = 6
    print(letters_in_word)
    print("You have ", lives, " lives remaining.")
    while lives_left == True:
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
        print(guess_formatted)
        for i in range (0,len(letters_in_word)):
            if guess_formatted == letters_in_word[i]:
                print(letters_in_word, guess_formatted)
                game_board[i] = letters_in_word[i]
                print(game_board)

        
def game(final_word):
    game_board =[]
    word_formatted = final_word.replace("\n","")
    word_length = len(word_formatted)
    for i in range(0,word_length):
        letters_in_word.append(word_formatted[i])
        game_board.append("_ ")
    print(game_board)
    playing(word_length, letters_in_word)
        
        
def select_word():
    Word_list = open("Classwork/Hangman/Word_list.txt","r")
    for i in range(1,97):
        Word_list_number = Word_list.readline()
        words.append(Word_list_number)
    final_word = words[random.randint(1,len(words))]
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
