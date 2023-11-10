option = 0
def add(num1,num2):#add x and y passes the values
    print(num1+num2)           
    menu()
def sub(num1,num2):#subtract
    print(num1-num2)
    menu()
def multiply(num1,num2):#multiply
    print(num1*num2)
    menu()
def divide(num1,num2):#divide
    print(num1/num2)
    menu()

def menu():
    option = int(input("What do you want to do? \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n"))
    num1 = int(input("Input your first number: "))
    num2 = int(input("Input your second number: "))#assigns the values
    if option == 1:
        add(num1,num2)
    elif option == 2:
        sub(num1,num2)
    elif option == 3:
        multiply(num1,num2)
    elif option == 4:
        divide(num1,num2)
    else:
        print("Please choose valid option>")
        menu()#starts again to do multiple calculations

menu()#starts the program
