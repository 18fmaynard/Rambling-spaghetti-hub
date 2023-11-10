names = ["James", "Joeseph", "Miles", "Logan", "Finn", "George"]
for i in range(0,len(names) - 1):
    for j in range(len(names)- 1 - i):
        if names[i] > names[j + 1]:
            name= names[j]
            names[j] = names[j + 1]
            names[j + 1] = names
            print(names)