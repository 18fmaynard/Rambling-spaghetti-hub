user_choice = str(input("Which gate would you like to choose: AND, NOT, OR, XOR?"))
if user_choice == "AND":
    num_1 = int(input("What is your first number (1 or 0):"))
    num_2 = int(input("What is your second number (1 or 0):"))
    if num_1 == 1:
        if num_2 == 1:
            print("1")
        else:
            print("0")
    else:
        print("0")
elif user_choice == "NOT":
    num_1 = int(input("What is your number (1 or 0):"))
    if num_1 == 1:
        print("0")
    else:
        print("1")
elif user_choice == "OR":
    num_1 = int(input("What is your first number (1 or 0):"))
    num_2 = int(input("What is your second number (1 or 0):"))
    if num_1 == 1:
        print("1")
    elif num_2 == 1:
        print("1")
    else:
        print("0")
elif user_choice == "XOR":
    num_1 = int(input("What is your first number (1 or 0):"))
    num_2 = int(input("What is your second number (1 or 0):"))
    if num_1 == 1:
        if num_2 == 0:
            print("1")
        else:
            print("0")
    elif num_2 == 1:
        if num_1 == 0:
            print("1")
        else:
            print("0")
    else:
        print("0")