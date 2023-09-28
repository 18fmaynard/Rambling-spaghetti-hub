import random
temperatures = []
for i in range (0,365):
    random_number = random.randint(0,40)
    temperatures.append(random_number)
Band_A = 0
Band_B = 0
Band_C = 0
Band_D = 0
for i in range(0,365):
    temperature = temperatures[i]
    if temperature <= 10:
        Band_A = Band_A + 1
    elif 11 <= temperature <= 20:
        Band_B = Band_B + 1
    elif 21 <= temperature <= 30:
        Band_C = Band_C + 1
    else:
        Band_D = Band_D + 1
print("Band A:", Band_A)
print("Band B:", Band_B)
print("Band C:", Band_C)
print("Band D:", Band_D)
