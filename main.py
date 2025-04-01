from collections import Counter
from random import randint

# testing23412342342423

def random_tile():
        global tile_list
        return tile_list[randint(1,len(tile_list)-1)]
def draw_tiles():
    global tile_list
    global num_players
    global player_tiles
    
    for i in range(7):
        
        for i in range(num_players):
            player_tiles[i].append(random_tile())
    return player_tiles



def main():
    # testing hello
    # testing gitdoc
    print("Welcome to Scrabble!")
    #get the values 
    num_players_valid = False
    while num_players_valid == False:
        try:
            num_players = int(input("How many players are playing?"))
            if num_players < 2 or num_players > 4:
                print("Invalid input, number of players must be between 2 and 4")
            else:
                num_players_valid = True
        except ValueError:
            print("Invalid input, please enter a whole number 1 - 4")
        


    win_condition_valid = False
    while win_condition_valid == False:
        try:
            win_condition = int(input("What do you want to be the win condition? \n Enter 1 for until all tiles are drawn \n Enter 2 for a certain number of moves \n Enter 3 for reaching a certain score"))
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

    player_turn = 1



    player_tiles = draw_tiles()           
            
    print(player_tiles)
main()