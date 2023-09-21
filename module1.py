# This program calculates if a given number is even or odd, and also checks if it's divisible by 3.
number = int(input("Enter a number: "))# Input: User enters a number
if number % 2 == 0:# Check if the number is even or odd
    even = True
else:
    even = False
divisible_3 = number % 3 == 0# Check if the number is divisible by 3

# Output the results
if even:
    print(number, " is even.")
else:
    print(number, " is odd.")

if divisible_3:
    print(number, "is divisible by 3.")
else:
    print(number, "is not divisible by 3.")
