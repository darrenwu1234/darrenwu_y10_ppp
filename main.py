from collections import Counter
from random import randint
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
def get_move_type(): 
    move_type_valid = False
    while move_type_valid == False:
        move_type = input("What move type do you want? \n Enter 1 to move a tile on your rack to the board \n Enter 2 to move a tile on the rack to a different square on the rack\n Enter 3 to move a tile on the board to a different square on the board\n Enter 4 to move a tile on the board to a position on your rack")
        if move_type != "1" and move_type != "2" and move_type != "3" and move_type != "4":
            print("Invalid input, please enter either 1,2,3 or 4: ")
        else:
            move_type_valid = True
    
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
                
            

            
    return origin
        
def get_move(): 
    
    move_type = get_move_type() 
    
    origin = get_origin(move_type)
    
    destination = get_destination(move_type) 
    return move_type, origin, destination
    #update_board()
def get_destination(move_type): 
    valid_move = False
    destination = input("Please enter where you want to place your tile") 
    if move_type == "1" or move_type == "3":
        while valid_move == False:
            if len(destination) == 2 or len(destination) == 3:
                
                if destination[0].upper() not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"] or destination[1:] not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]:

                    print("Not a valid position, please enter a letter A-P followed by a number 1-16 e.g(D13)")
                    destination = input("Enter the position where you want to draw your tile from: ") 
                else:
                    valid_move = True
            else:
                print("Not a valid position, please enter a letter A-P followed by a number 1-16 e.g(D13)")
                origin = input("Enter the position where you want to draw your tile from: ")
    else:
        if destination not in ["1","2","3","4","5","6","7"]:

            print("Not a valid position, please input a number")

            destination = input("Please enter where you want to place your tile")
        
    return destination
global player_turn
player_turn = 0
def show_tiles():
    print(player_tiles)
    print(f"Player {player_turn + 1 }'s tiles: ")
    print("1   2   3   4   5   6   7")
    for i in player_tiles[player_turn]:

        print(i, end = "   ")      
    print("")
def show_info():
    print(f"Player {player_turn +1}'s turn!")
    show_board()
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
    
def show_move(board,player_tiles,move_type,origin,destination):
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
        print(f"Tile {tile} moved from {origin} to {destination.upper()}.")
    return tile


   



def update_board(board, tile, destination,move_type,player_tiles):
    if move_type == "1" or move_type == "3":
        row_num = int(destination[1:]) - 1
        column_num = destination[0]
        column_num = ord(column_num.upper()) - 65
        board[row_num][column_num] = tile
    else:
        player_tiles[player_turn][int(destination)-1] = tile
    
def replace_tile(player_tiles):
    r_tile = random_tile(tile_list)
    for i in player_tiles[player_turn]:
        if i == " ":
            i = r_tile
    print(f"{r_tile} was drawn")
    show_tiles()
    
    
def player_move():
    turn_submitted = False
    while turn_submitted == False:
        show_info()
        move_type, origin, destination = get_move()
        tile = show_move(board,player_tiles,move_type,origin,destination)
        update_board(board, tile, destination,move_type,player_tiles)
        show_board()
    replace_tile(player_tiles)
    





# testing hello
# testing gitdoc
print("Welcome to Scrabble!")
#get the values 
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
    player_move()      
    player_turn += 1
    
    player_turn = player_turn % num_players
    key_input = input("Enter any key to move on to the next turn")
    