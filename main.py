class Piece:
    def __init__(self,piece,value):
        self.piece = piece
        self.value = value
    def double_value(self):
        pass
#class EmptyPiece(Piece):
class EmptyPiece(Piece):
    def __init__(self):
        super().__init__("None",0)
class Board:
    def __init__(self,board = None):
        if board == None:
            self.board = self.create_board()
        else:
            self.board = board
    def create_board(self):
        board = []
        for _ in range(16):
            row = []
            
            for _ in range(16):
                row.append(EmptyPiece())
            board.append(row)
        return board
    def add_tile(self,row,column,piece):
        self.board[row][column] = piece
    def remove_tile(self,row,column):
        print(f"{self.board[row][column].piece} removed from {row}{column}")
        self.board[row][column] = EmptyPiece()
        
    def double_value(self,row,column):
        piece = self.board[row][column]
        piece.value *= 2
        self.board[row][column] = piece
    def display_board(self):
        row_num = 1
        print("   A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P")
        for row in self.board:
            if row_num < 10:
                print(" " + str(row_num), end = "")
            else:
                print(row_num, end = "")
            for item in row:
                
                if item.piece != "None":
                    print(f"[{item.piece}]",end = "")
                else:
                    print("[ ]",end = "")
            row_num+=1
                
            print("")
    def display_values(self):
        for row in self.board:
            for item in row:
                print(f"[{item.value}]",end = "")
            print("")
    def display_value(self,row,column):
        piece = self.board[row][column]
        print(piece.value)
    def check_same_column(self,temp_board):
        is_column = True
        for i in temp_board:
            if temp_board[0].column != i.column:
                is_column = False
        #print("column",is_column)
        return is_column
    def check_same_row(self,temp_board):
        is_row = True
        for i in temp_board:
            if temp_board[0].row != i.row:
                is_row = False
        #print("row",is_row)
        return is_row
    def check_increment(self,temp_board,is_column,is_row):
        if is_column == True:
        
            for i in range(1,len(temp_board)):
                if temp_board[0].row + i != temp_board[i].row:
                    is_row = False
        elif is_row == True:
            
            for i in range(1,len(temp_board)):
                if temp_board[0].column + i != temp_board[i].column:
                    is_column = False
        return is_row, is_column
    def check_straight(self):
        row_count = 0
        
        self.temp_board = []
        for row in self.board:
            column_count = 0
            
            for i in row:
                
                if i.value != 0:
                    self.temp_board.append(Piece_and_Position(i.piece,i.value,row_count,column_count))
                column_count += 1
            row_count += 1
        
        a1 = False
        a2 = False
        if self.check_same_column(self.temp_board) == True:
            self.temp_board.sort(key=lambda x: x.row)
            a1, a2 = self.check_increment(self.temp_board,True,False)
        elif self.check_same_row(self.temp_board) == True:
            self.temp_board.sort(key=lambda x: x.column)
            a1, a2 = self.check_increment(self.temp_board,False,True)
        if a1 == True or a2 == True:
            self.valid_output = self.valid_word()
        else:
            self.valid_output = False
    def valid_word(self):
        word = ""
        for i in self.temp_board:
            word += i.piece
            print(word)
        if word in game.dictionary_set:
            valid_output = True
        else:
            valid_output = False
        return valid_output
    
        
            
        
            
        
    def perform_move(self):
        input_value = Inputs()
        
        input_value.perform_move_type()
            


class Piece_and_Position:
    def __init__(self,piece,value,row,column):
        self.piece = piece
        self.value = value
        self.row = row
        self.column = column
    
class Inputs:
    def __init__(self):
        pass
    def ask_move_type(self):
        move_type_valid = False
        while move_type_valid == False:
            move_type = input("What move type do you want? \n Enter 1 to move a tile on your rack to the board \n Enter 2 to move a tile on the rack to a different square on the rack\n Enter 3 to move a tile on the board to a different square on the board\n Enter 4 to move a tile on the board to a position on your rack\n Enter 'S' to submit your word\n Enter 'I' to see information")
            if move_type not in ['1','2','3','4'] and move_type.upper() not in ['S','I']:
                print("Move type invalid, please enter a valid input")
            else:
                move_type_valid == True
                return move_type
    def get_origin(self,move_type):  
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
    def get_desintation(self,move_type):
        
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


    def perform_move_type(self):
        move_type = self.ask_move_type()
        
        if move_type != "S" and move_type != "I":
            
            origin = self.get_origin(move_type)
            destination = self.get_desintation(move_type)
            game.perm_board.board = self.update_board(origin,destination,move_type,game.info.player_turn,game.perm_board.board,game.player_tiles.player_tiles)
        #print(player_tiles.player_tiles)
        #print(player_tiles.tile_list)
        elif move_type == "S":
            self.submit(game.perm_board.valid_output)
    def submit(self,valid_output):
        if valid_output == True:
            print("submitted")
        else:
            print("bad")

    def update_board(self,origin,destination,move_type,player_turn,perm_board,player_tiles):
        
        
        if move_type == "1":
            tile = player_tiles[player_turn][int(origin) - 1]
            player_tiles[player_turn][int(origin) - 1] = EmptyPiece()
            print(f"Tile {tile.piece} moved from {origin} to {destination.upper()}.")
            row_num = int(destination[1:]) - 1
            column_num = destination[0]
            column_num = ord(column_num.upper()) - 65
            perm_board[row_num][column_num] = tile
        elif move_type == "2":
            tile = player_tiles[player_turn][int(origin) - 1]
            tile2 = player_tiles[player_turn][int(destination) - 1] 
            player_tiles[player_turn][int(origin) - 1] = tile2
            player_tiles[player_turn][int(destination) - 1] = tile
        elif move_type == "3":
            row_num = int(origin[1:]) - 1
            column_num = origin[0]
            column_num = ord(column_num.upper()) - 65
            #print('AIHSODFHASODFHO')
            #print(game.perm_board.temp_board)
            for i in game.perm_board.temp_board:
                #print(i.row,i.column,row_num,column_num)
                if i.row == row_num and i.column == column_num:
                    tile = i
                    
            perm_board[row_num][column_num] = EmptyPiece()
            destination_column = ord(destination[0].upper())-65
            print(f"Tile {tile.piece} moved from {origin} to {destination.upper()}.")
            
            perm_board[int(destination[1:])-1][destination_column] = tile
        elif move_type == "4":
            row_num = int(origin[1:]) - 1
            column_num = origin[0]
            column_num = ord(column_num.upper()) - 65
            for i in game.perm_board.temp_board:
                #print(i.row,i.column,row_num,column_num)
                if i.row == row_num and i.column == column_num:
                    tile = i
                    
            perm_board[row_num][column_num] = EmptyPiece()
            
            print(f"Tile {tile.piece} moved from {origin} to {destination.upper()}.")
            
            
            player_tiles[player_turn][int(destination)-1] = tile
        return perm_board
        
      
        
            

        
class Tiles:
    def __init__(self,player_turn,num_players,player_tiles = None):
        self.player_turn = player_turn
        self.num_players = num_players
        
        if player_tiles == None:
            
            tile_list, self.player_tiles = self.create_tile_list()
        else:
            self.player_tiles = player_tiles
        self.tile_list = tile_list
    def display_tiles(self,player_turn):
        
        
        print(f"Player {player_turn + 1 }'s tiles: ")
        print("Tile Number - 1   2   3   4   5   6   7")
        print("              ", end = "")
        for i in self.player_tiles[player_turn]:

            if i.piece != "None":
                print(i.piece, end = "   ")      
            else:
                print(" ", end = "   ")
        print("")
        print("Tile Values - ",end = "")
        for i in self.player_tiles[player_turn]:
            try:
                if i.value == 0:
                    print(" ", end = "   ")
                elif i.value != 10:
                    print(i.value,end = "   ")
                else:
                    print(i.value,end = "  ")
            except:
                print(" ",end = "   ")
        print("")
        
    def draw_tiles(self,tile_list,player_tiles):
        
        for i in range(7):
            
            for i in range(self.num_players):
                
                tile_list, random_tile_object = self.random_tile(tile_list)
                
                player_tiles[i].append(random_tile_object)
        return tile_list, player_tiles
    def create_tile_list(self):
        from collections import Counter
        counter_tile_list = Counter({Piece("A",1) : 9, Piece("B",3): 2, Piece("C",3): 2, Piece("D",2) : 4, Piece("E",1): 12, Piece("F",4): 2,Piece("G",2): 3,Piece("H",4): 2, Piece("I",1): 9, Piece("J",8): 1, Piece("K",5): 1, Piece("L",1): 4,Piece("M",3): 2, Piece("N",1): 6, Piece("O",1): 8, Piece("P",3): 2, Piece("Q",10): 1, Piece("R",1): 6, Piece("S",1): 4, Piece("T",1): 6, Piece("U",1): 4, Piece("V",4): 2, Piece("W",4): 2, Piece("X",8): 1, Piece("Y",4): 2, Piece("Z",10): 1})
        tile_list = []
        for i in counter_tile_list.elements():
            tile_list.append(i)
        player_tiles = []
        for i in range(self.num_players):
            player_tiles.append([])
        
        tile_list, player_tiles = self.draw_tiles(tile_list,player_tiles)  
        
        return tile_list, player_tiles
    
    def random_tile(self,tile_list):
        from random import randint
        
        random_tile = tile_list.pop(randint(1,len(tile_list)-1))
        return tile_list, random_tile
class Information:
    def __init__(self,player_turn = None):
        if player_turn == None:
            self.player_turn = 0
        else:
            self.player_turn = player_turn
class Main:
    def __init__(self,info = None,perm_board = None,player_tiles = None,dictionary_set = None):
        if info == None:
            self.info = Information()
        else:
            self.info = info
        if perm_board == None:
            self.perm_board = Board()   
        else:
            self.perm_board = perm_board
        if player_tiles == None:
            self.player_tiles = Tiles(0,2)
        else:
            self.player_tiles = player_tiles
        if dictionary_set == None:
            self.dictionary_set= set(line.strip() for line in open('dictionary.txt'))
        else:
            self.dictionary_set = dictionary_set
    def player_move(self):    
        
        self.perm_board.perform_move()
        self.perm_board.display_board()
        self.player_tiles.display_tiles(self.info.player_turn)
        self.perm_board.check_straight()
    def player_turn(self):
        self.perm_board.display_board()
        
        self.player_tiles.display_tiles(self.info.player_turn)
        while True:
            game.player_move()
            
game = Main()
game.player_turn()
