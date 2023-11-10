def multiply(x,y):
    z = x * y
    a = ("The answer is:")
    return a, z

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
answer = multiply(num1, num2)
print(answer[0])
print(answer[1])