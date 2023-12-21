import print_board

def rings_choice():
    valid_rings = False
    print("How many rings would you like to use (3-8)?")
    num_rings = str(input())
    if num_rings.isdigit():
        num_rings = int(num_rings)
        if 3<= num_rings <=8:
            set_board(num_rings)
        else:
            print("Invalid")
            rings_choice()
    else:
        valid_strings = ["three", "four", "five", "six", "seven", "eight"]
        for i in range(6):
            if num_rings.lower() == valid_strings[i]:
                num_rings = i + 3
                print(num_rings)
                valid_rings = True
                set_board(num_rings)
                break
        if valid_rings == False:
            print("Invalid")
            rings_choice()

def set_board(num_rings):
    moves = 0
    tower_1 = []
    tower_2 = []
    tower_3 = []
    for i in range(0, num_rings):
        tower_1.append(i + 1)
    print_board.print_board(tower_1, tower_2, tower_3, moves)
    make_move(tower_1, tower_2, tower_3, moves, num_rings)
    
def make_move(tower_1, tower_2, tower_3, moves, num_rings):
    start_tower_valid = False
    end_tower_valid = False
    print("Which tower would you like to remove a ring from (1, 2, 3)?")
    start_tower = input()
    if start_tower.isdigit():
        start_tower = int(start_tower)
        if start_tower < 1 or start_tower > 3:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    else:
        valid_strings = ["one", "two", "three"]
        for i in range(3):
            if start_tower.lower() == valid_strings[i]:
                start_tower = i + 1
                start_tower_valid = True
                break
        if start_tower_valid == False:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    if start_tower == 1:
        if len(tower_1) == 0:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    elif start_tower == 2:
        if len(tower_2) == 0:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    elif start_tower == 3:
        if len(tower_3) == 0:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    print("Which tower would you like to move this ring to (1, 2, 3)?")
    end_tower = input()
    if end_tower.isdigit():
        end_tower = int(end_tower)
        if end_tower < 1 or end_tower > 3:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    else:
        valid_strings = ["one", "two", "three"]
        for i in range(3):
            if end_tower.lower() == valid_strings[i]:
                end_tower = i + 1
                end_tower_valid = True
                break
        if end_tower_valid == False:
            print("Invalid")
            make_move(tower_1, tower_2, tower_3, moves, num_rings)
    if end_tower == start_tower:
        print("Invalid")
        make_move(tower_1, tower_2, tower_3, moves, num_rings)  
    if end_tower == 1:
        if len(tower_1) == 0:
            change_towers(start_tower, end_tower, tower_1, tower_2, tower_3, moves, num_rings)
        if start_tower == 2:
            if tower_2[len(tower_2)-1] < tower_1[len(tower_1)-1]:
                print("Invalid")
                make_move(tower_1, tower_2, tower_3, moves, num_rings)
        if start_tower == 3:
            if tower_3[len(tower_3)-1] < tower_1[len(tower_1)-1]:
                print("Invalid")
                make_move(tower_1, tower_2, tower_3, moves, num_rings)
    elif end_tower == 2:
        if len(tower_2) == 0:
            change_towers(start_tower, end_tower, tower_1, tower_2, tower_3, moves, num_rings)
        if start_tower == 1:
            if tower_1[len(tower_1)-1] < tower_2[len(tower_2)-1]:
                print("Invalid")
                make_move(tower_1, tower_2, tower_3, moves, num_rings)
        if start_tower == 3:
            if tower_3[len(tower_3)-1] < tower_2[len(tower_2)-1]:
                print("Invalid")
                make_move(tower_1, tower_2, tower_3, moves, num_rings)
    elif end_tower == 3:
        if len(tower_3) == 0:
            change_towers(start_tower, end_tower, tower_1, tower_2, tower_3, moves, num_rings)
        if start_tower == 1:
            if tower_1[len(tower_1)-1] < tower_3[len(tower_3)-1]:
                print("Invalid")
                make_move(tower_1, tower_2, tower_3, moves, num_rings)
        if start_tower == 2:
            if tower_2[len(tower_2)-1] < tower_3[len(tower_3)-1]:
                print("Invalid")
                make_move(tower_1, tower_2, tower_3, moves, num_rings)
    change_towers(start_tower, end_tower, tower_1, tower_2, tower_3, moves, num_rings)
        
def change_towers(start_tower, end_tower, tower_1, tower_2, tower_3, moves, num_rings):
    if start_tower == 1:
        if end_tower == 2:
            tower_2.append(tower_1[len(tower_1)-1])
            tower_1.pop()
        elif end_tower == 3:
            tower_3.append(tower_1[len(tower_1)-1])
            tower_1.pop()
    elif start_tower == 2:
        if end_tower == 1:
            tower_1.append(tower_2[len(tower_2)-1])
            tower_2.pop()
        elif end_tower == 3:
            tower_3.append(tower_2[len(tower_2)-1])
            tower_2.pop()
    elif start_tower == 3:
        if end_tower == 1:
            tower_1.append(tower_3[len(tower_3)-1])
            tower_3.pop()
        elif end_tower == 2:
            tower_2.append(tower_3[len(tower_3)-1])
            tower_3.pop()
    moves = moves + 1
    if len(tower_3) == num_rings:
        finnish(tower_1, tower_2, tower_3, moves)
    print_board.print_board(tower_1, tower_2, tower_3, moves)
    
    make_move(tower_1, tower_2, tower_3, moves, num_rings)
    
def finnish(tower_1, tower_2, tower_3, moves):
    print_board.print_board(tower_1, tower_2, tower_3, moves)
    print("Do you want to play again?")
    play_again = str(input())
    if play_again.lower() == "yes":
        rings_choice()
    else:
        exit()

####starts here####
print("Welcome to the towers of hanoi!") 
rings_choice()