correct = False
while correct == False:#while loop used so that if they enter the wrong input it repeates
    opinion = input("Input Yes or NO?")
    if opinion == "Yes":#if the input they provide is correct it ends the loop
        correct = True
    else:#if they enter the wrong input it repeats the loop
        print("Wrong, try again.")
for i in range(0,10):#using a for loop becuase the task said to
    print("YAY!")
