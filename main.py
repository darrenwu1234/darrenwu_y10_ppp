from collections import Counter
from random import randint
dictionary_set = set(line.strip() for line in open('dictionary.txt'))

value_dict = {"A" : 1, "B": 3, "C": 3, "D" : 2, "E": 1, "F": 4,"G": 2,"H": 4, "I": 1, "J": 8, "K": 5, "L": 1,"M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

board = []
for i in range(16):
    
    board.append([])
for i in range(len(board)):
    for f in range(16):
        board[i].append(" ")

def random_tile(tile_list):
 
    random_tile = tile_list.pop(randint(1,len(tile_list)-1))
    return random_tile
def draw_tiles(tile_list):
    
    global num_players
    
    for i in range(7):
        
        for i in range(num_players):
            player_tiles[i].append(random_tile(tile_list))
    return player_tiles

def get_move_type(valid_output, word, word_score,player_scores,player_turn): 
    move_type_valid = False
    while move_type_valid == False:
        move_type = input("What move type do you want? \n Enter 1 to move a tile on your rack to the board \n Enter 2 to move a tile on the rack to a different square on the rack\n Enter 3 to move a tile on the board to a different square on the board\n Enter 4 to move a tile on the board to a position on your rack\n Enter 5 to submit your word")
        if move_type != "1" and move_type != "2" and move_type != "3" and move_type != "4" and move_type != "5":
            print("Invalid input, please enter either 1,2,3 or 4: ")
        else:
            move_type_valid = True
        if move_type == "5":
            move_type_valid = submit(valid_output, word, word_score,player_scores,player_turn)

    
    return move_type 

 

def get_origin(move_type):  
    valid_move = False
    
    

  

    if move_type == "1" or move_type == "2":
        origin = input("Enter the position where you want to draw your tile from: ")

        while origin not in ["1","2","3","4","5","6","7"]: 
            

            print("Not a valid position, please enter a number 1-7")
            origin = input("Enter the position where you want to draw your tile from: ") 

            

        


    elif move_type == "3" or move_type == "4":
        origin = input("Enter the position where you want to draw your tile from: ") 

        while valid_move == False:
            if len(origin) == 2 or len(origin) == 3:
                
                if origin[0].upper() not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"] or origin[1:] not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]:

                    print("Not a valid position, please enter a letter A-P followed by a number 1-16 e.g(D13)")
                    origin = input("Enter the position where you want to draw your tile from: ") 
                else:
                    valid_move = True
            else:
                print("Not a valid position, please enter a letter A-P followed by a number 1-16 e.g(D13)")
                origin = input("Enter the position where you want to draw your tile from: ")
                
            

    try:
        return origin
    except:
        pass
        
def get_move(valid_output, word, word_score,player_scores,player_turn): 
    
    move_type = get_move_type(valid_output, word, word_score,player_scores,player_turn) 
    
    if move_type != "5":
        origin = get_origin(move_type)
        
        destination = get_destination(move_type) 
        return move_type,origin, destination
    else:
        return move_type, 0, 0
    #update_board()
def get_destination(move_type): 
    valid_move = False
    destination = input("Please enter where you want to place your tile") 
    if move_type == "1" or move_type == "3":
        while valid_move == False:
            if len(destination) == 2 or len(destination) == 3:
                
                if destination[0].upper() not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"] or destination[1:] not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]:
                    print(destination[0])
                    print(destination[1:])
                    print("Not a valid position, please enter a letter A-P followed by a number 1-16 e.g(D13)")
                    destination = input("Enter the position where you want to place your tile: ") 
                else:
                    valid_move = True
            else:
                print("Not a valid position, please enter a letter A-P followed by a number 1-16 e.g(D13)")
                destination = input("Enter the position where you want to place your tile: ")
    else:
        while valid_move == False:
            if destination not in ["1","2","3","4","5","6","7"]:

                print("Not a valid position, please input a number")

                destination = input("Please enter where you want to place your tile")
            else:
                valid_move = True
    try:
        return destination
    except:
        pass
global player_turn
player_turn = 0
def show_tiles():
   
    print(f"Player {player_turn + 1 }'s tiles: ")
    print("Tile Number - 1   2   3   4   5   6   7")
    print("              ", end = "")
    for i in player_tiles[player_turn]:

        print(i, end = "   ")      
    print("")
    print("Tile Values - ",end = "")
    for i in player_tiles[player_turn]:
        try:
            if value_dict[i] != 10:
                print(value_dict[i],end = "   ")
            else:
                print(value_dict[i],end = "  ")
        except:
            print(" ",end = "   ")
    print("")

def show_info():
    
    
    show_tiles()

def show_board():
   
    
    print(f"Current board: ")
    row_num = 1
    print("   A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P")
    for i in range(len(board)):
        if row_num < 10:
            row_char = " " + str(row_num)
        else:
            row_char = str(row_num)
        print(row_char + "[" + "][".join(board[i])+"]")
        row_num += 1
    
def show_move(board,player_tiles,move_type,origin,destination,temp_board):
    if move_type == "1" or move_type == "2":
        tile = player_tiles[player_turn][int(origin) - 1]
        player_tiles[player_turn][int(origin) - 1] = " "
        print(f"Tile {tile} moved from {origin} to {destination.upper()}.")
    else:
        row_num = int(origin[1:]) - 1
        column_num = origin[0]
        column_num = ord(column_num.upper()) - 65
        tile = board[row_num][column_num]
        board[row_num][column_num] = " "
        temp_board.remove([tile,row_num,column_num])
        print(f"Tile {tile} moved from {origin} to {destination.upper()}.")
    return tile


   



def update_board(board, tile, destination,move_type,player_tiles,temp_board):
    if move_type == "1" or move_type == "3":
        row_num = int(destination[1:]) - 1
        column_num = destination[0]
        column_num = ord(column_num.upper()) - 65
        board[row_num][column_num] = tile
        temp_board.append([tile,row_num,column_num])
    else:
        
        player_tiles[player_turn][int(destination)-1] = tile
        
    
    
def replace_tile(player_tiles):
    
    for i in range(len(player_tiles[player_turn])):
        r_tile = random_tile(tile_list)
        if player_tiles[player_turn][i] == " ":
            player_tiles[player_turn][i] = r_tile
            print(f"{r_tile} was drawn")
    show_tiles()
    
    
def player_move(player_tiles):
    print(f"Player {player_turn +1}'s turn!")
    temp_board = []
    turn_submitted = False
    show_board()
    valid_output = False
    word = ""
    word_score = 0
    while turn_submitted == False:
        show_info()

        move_type, origin, destination = get_move(valid_output, word, word_score,player_scores,player_turn)
        if move_type != "5":

            tile = show_move(board,player_tiles,move_type,origin,destination,temp_board)
            update_board(board, tile, destination,move_type,player_tiles,temp_board)
            show_board()
            valid_output, word, word_score = is_valid_output(temp_board)
        else:
            turn_submitted = True
        
    replace_tile(player_tiles)

def submit(valid_output, word, word_score,player_scores,player_turn):
    valid_input = False
    if valid_output == True:
        
        while valid_input == False:
            is_submit = input("Do you want to submit your turn? y/n")
            if is_submit.upper() == "YES" or is_submit.upper() == "Y" or is_submit.upper() == "YE" or is_submit.upper() == "YS" or is_submit.upper() == "YEAH":
                is_submit = True
                valid_input = True
                
            elif is_submit.upper() == "NO" or is_submit.upper() == "N" or is_submit.upper() == "NAH" or is_submit.upper() == "NOPE" or is_submit.upper() == "N O":
                is_submit = False
                valid_input = True
                
            if valid_input == False:
                print('Invalid input, please enter y for yes, or n for no')
    
    else:
        is_submit = False
        
        print("Word is not valid, so you cannot submit it.")
        

    if is_submit == True:
        
        player_scores[player_turn] = int(player_scores[player_turn][0])  + word_score
        print(f"{word} submitted for {word_score} points, Player {player_turn + 1}'s score is now {player_scores[player_turn]}")
        
        return True
    else:
        return False
def is_valid_output(temp_board):
    word_score = 0
    valid_output, is_column,is_row = is_straight(temp_board)
    word = ""
    
    if valid_output == True:
        
        if is_column == True:
            temp_board.sort(key=lambda x: x[1]) 
        elif is_row == True:
            temp_board.sort(key=lambda x: x[2])
        print("Current word score")
        for i in temp_board:
            word += i[0]
            word_score += value_dict[i[0]]
           
            print(f"{i[0]} - {value_dict[i[0]]}")
        print(f"Total word score is - {word_score}")
        if word in dictionary_set:
            valid_output = True
            print("Word is valid")
        else:
            valid_output = False
            print("Word is not valid, the word you have inputed is not a real word")
    
    
    else:
        print("Word is not valid, it is not in a straight line")
    return valid_output, word, word_score
       
def is_straight(temp_board):
    valid_output = True
    temp_row_list = []
    temp_column_list = []
    for i in temp_board:
        temp_row_list.append(i[1])
        temp_column_list.append(i[2])
    temp_row_list.sort()
    temp_column_list.sort()
    g = 0
    
    is_row = True
    for i in range(len(temp_row_list)):
        if temp_row_list[0] != temp_row_list[i]:
            
            is_row = False
    is_column = True
    for i in range(len(temp_column_list)):
        if temp_column_list[0] != temp_column_list[i]:
            is_column = False
    if is_column == True:
        
        for f in range(1,len(temp_row_list)):
            if valid_output == True:
                g += 1
                if temp_row_list[0]+g == temp_row_list[f]:
                    valid_output = True
                else:
                    valid_output = False
    elif is_row == True:
        
        for f in range(1,len(temp_column_list)):
            if valid_output == False:
                g += 1
                if temp_column_list[0]+g == temp_column_list[f]:
                    valid_output = True
                else:
                    valid_output = False
    else:
        valid_output = False    
                        
                

    return valid_output,is_column,is_row    





# testing hello
# testing gitdoc
print("Welcome to Scrabble!")
#get the values 
player_scores = []
num_players_valid = False
while num_players_valid == False:
    try:
        num_players = int(input("How many players are playing? "))
        if num_players < 2 or num_players > 4:
            print("Invalid input, number of players must be between 2 and 4")
        else:
            num_players_valid = True
    except ValueError:
        print("Invalid input, please enter a whole number 1 - 4")
    for i in range(num_players):
            player_scores.append([0])


win_condition_valid = False
while win_condition_valid == False:
    try:
        win_condition = int(input("What do you want to be the win condition? \n Enter 1 for until all tiles are drawn \n Enter 2 for a certain number of moves \n Enter 3 for reaching a certain score "))
        if win_condition < 1 or win_condition > 3:
            print("Invalid input, number must be between 1 - 3")
        else:
            win_condition_valid = True
    except ValueError:
        print("Invalid input, please enter a whole number between 1 - 3")
# more testing

#
counter_tile_list = Counter({"A" : 9, "B": 2, "C": 2, "D" : 4, "E": 12, "F": 2,"G": 3,"H": 2, "I": 9, "J": 1, "K": 1, "L": 4,"M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1})
tile_list = []
for i in counter_tile_list.elements():
    tile_list.append(i)

player_tiles = []
for i in range(num_players):
    player_tiles.append([])




player_tiles = draw_tiles(tile_list)  
while True:          
    print(player_scores)
    player_move(player_tiles)      
    player_turn += 1
    player_turn = player_turn % num_players
    key_input = input("Enter any key to move on to the next turn")
    