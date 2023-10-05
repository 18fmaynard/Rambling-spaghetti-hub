array = []#setting values for varisables and the array
team_1 = 0
team_1_total = 0
total = 0

players = int(input("How many players are there?: "))#asks how many players there are

for i in range(0,players):#repeats the same amount of times that there are players
    print("Player", i + 1)#prints out which player is entering information
    team = int(input("Which team are you on:\n1. Red\n2. Green\n Team: "))#asks which team they are on
    if 1 <= team <= 2:#makes sure value is within expected values
        score = int(input("What was your score? "))#asks them for there score
        array.append([team,score])#saves their team and score into the array
        array.sort()#sorts the array so that all team 1 players are at the begginning
        print(array)#prints the array
        if team == 1:
            team_1 = team_1 + 1#if the team is one it adds one to the ammount from team one to be used in a looplater
    else:
        print("incorrect input!")#if there valuye is not in the expected range it does this
        players = players + 1#it adds one to the amount of times it does the loop so that it can disregard this player ans still end with the expected amount of players

for i in range(0,players):#repeates the number of times there are players
    player_i_t = array[i]#seperates an individual part of the 2D array as a list
    total_score = player_i_t[1]#finds the score in this part of the array
    total = total + total_score#adds this score to the tatol for the whole thing until it has the total score overall

for i in range(0,team_1):#repeats for the number of people in team one
    player_i_1 = array[i]#reads the values from the start of the array as due to the sort these are all from team 1
    player_i_1_score = player_i_1[1]#saves the score of the player from team one
    team_1_total = team_1_total + player_i_1_score#adds the scores from each team one player to get a total for the team
    
team_2_total = total - team_1_total#finds total for team 2 by taking team 1 total from game total

print("Red team scored:",team_1_total)#prints each teams score
print("Green team scored:",team_2_total)
if team_1_total > team_2_total:#checks which team has a higher score and prints which team won or if it was a draw
    print("Red team wins!")
elif team_1_total == team_2_total:
    print("You drew!")
else:
    print("Green team wins!")
