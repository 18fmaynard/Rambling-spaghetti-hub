interestrate = 1.1
years = 0
amount = int(input("How much do you want to put in each year?"))
amount_b = amount
years = int(input("How many years do you want to do this for?"))
for i in range(0,years):
	print("Year ", i + 1, "Start amount", amount)
	amount = amount * interestrate
	print("After interest", amount)
	amount = amount + amount_b
difference = amount - (amount_b * years)
print("You have ", amount)
print("Over", years,"years, you have gained ", difference, "in interest.")