import colorama
from colorama import Fore
colorama.init(autoreset = True)
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
    def __init__(self,board = None,valid_output = None,temp_board = None):
        if board == None:
            self.board = self.create_board()
        else:
            self.board = board
        if valid_output == None:
            self.valid_output = False
        else:
            self.valid_output = valid_output
        if temp_board == None:
            self.temp_board = []
        else:
            self.temp_board = temp_board
    def create_board(self):
        board = []
        for _ in range(15):
            row = []
            
            for _ in range(15):
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
        print("   A  B  C  D  E  F  G  H  I  J  K  L  M  N  O")
        row_count = 0
        
        for row in self.board:
            if row_num < 10:
                print(" " + str(row_num), end = "")
            else:
                print(row_num, end = "")
            column_count = 0
            for item in row:
                if row_count == 7 and column_count == 7:
                    if item.piece != "None" and game.user_board.board[row_count][column_count].piece != "None":
                        print(Fore.RED + "["+Fore.YELLOW + item.piece + Fore.RED + "]",end = "")
                    elif item.piece != "None":
                        print(Fore.RED + "["+Fore.RESET+item.piece+Fore.RED+"]",end = "")
                    else:
                        print(Fore.RED + "[ ]",end = "")
                    
                elif item.piece != "None" and game.user_board.board[row_count][column_count].piece != "None":
                    print("["+Fore.YELLOW + item.piece +Fore.RESET+"]",end = "")
                elif item.piece != "None":
                    print("["+item.piece+"]",end = "")
                
                
                else:
                    print("[ ]",end = "")
                column_count += 1
            row_num+=1
            row_count += 1
            
                
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
        correct = True
        if is_column == True:
        
            for i in range(1,len(temp_board)):
                if temp_board[0].row + i != temp_board[i].row:
                    correct = False
        elif is_row == True:
            
            for i in range(1,len(temp_board)):
                if temp_board[0].column + i != temp_board[i].column:
                    correct = False
        return correct
    def check_straight_second(self):
        
        row_count = 0
        
        self.temp_board = []
        for row in self.board:
            column_count = 0
            
            for i in row:
                
                if i.piece != "None":
                    self.temp_board.append(Piece_and_Position(i.piece,i.value,row_count,column_count))
                column_count += 1
            row_count += 1
        
        correct = True
        if self.check_same_column(self.temp_board) == True:
            column = self.temp_board[0].column
            self.temp_board.sort(key=lambda x: x.row)
            for i in range(self.temp_board[0].row,self.temp_board[-1].row):
                if game.total_board.board[i][column].piece == "None":
                    correct = False
                    print("word is seperated")
        elif self.check_same_row(self.temp_board) == True:
            row = self.temp_board[0].row
            self.temp_board.sort(key=lambda x: x.column)
            for i in range(self.temp_board[0].column,self.temp_board[-1].column):
                if game.total_board.board[row][i].piece == "None":
                    correct = False
                    print("word is seperated")
        else:
            correct = False
            print("Word is not in a straight line")

        if correct == True:
            self.valid_output = True
        else:
            self.valid_output = False
        return correct
            
            
            
    def check_straight(self):
        if game.total_board.board[7][7].piece == "None":
            self.pass_over_middle = False
        else:
            self.pass_over_middle = True
        row_count = 0
        
        self.temp_board = []
        for row in self.board:
            column_count = 0
            
            for i in row:
                
                if i.value != 0:
                    self.temp_board.append(Piece_and_Position(i.piece,i.value,row_count,column_count))
                column_count += 1
            row_count += 1
        
        correct = False
        if self.check_same_column(self.temp_board) == True:
            self.temp_board.sort(key=lambda x: x.row)
            correct = self.check_increment(self.temp_board,True,False)
        elif self.check_same_row(self.temp_board) == True:
            self.temp_board.sort(key=lambda x: x.column)
            correct = self.check_increment(self.temp_board,False,True)
        if correct == True:
            self.valid_word()
            if self.pass_over_middle == False:
                self.valid_output = False

                
                
                
        else:
            self.valid_output = False
        word = ""
        for i in self.temp_board:
            word += i.piece
            
            #self.word_score += i.value
            print(f"{i.piece} - {i.value}")
        
    def valid_word(self):
        word = ""
        self.word_score = 0
        for i in self.temp_board:
            word += i.piece
            
            self.word_score += i.value
            print(f"{i.piece} - {i.value}")
        print(f"Current word - {word}")
        print(f"Current word score - {self.word_score}")
        if word in game.dictionary_set:
            self.valid_output = True
        else:
            self.valid_output = False
       
    def update(self):
        
        for i in self.temp_board:
            row = i.row
            column = i.column
            temp_Piece = Piece(i.piece,i.value)
            self.board[row][column] = temp_Piece
            
    def mix(self):
        game.total_board = Board()
        for row in range(len(game.perm_board.board)):
            for column in range(len(game.perm_board.board)):
                if game.perm_board.board[row][column].piece != "None":
                    game.total_board.board[row][column] = game.perm_board.board[row][column]
        for row in range(len(game.user_board.board)):
            for column in range(len(game.user_board.board)):
                if game.user_board.board[row][column].piece != "None":
                    game.total_board.board[row][column] = game.user_board.board[row][column]
    def check_valid(self):
        row_count = 0
        
        self.temp_board = []
        for row in self.board:
            column_count = 0
            
            for i in row:
                
                if i.piece != "None":
                    self.temp_board.append(Piece_and_Position(i.piece,i.value,row_count,column_count))
                column_count += 1
            row_count += 1
        
        self.left_tile_list = []
        self.up_tile_list = []
        self.check_connected()
        if self.connected == True:
            for row in range(len(game.total_board.board)):
                for column in range(len(game.total_board.board[row])):
                    if game.total_board.board[row][column].piece != "None":
                        self.check_orientation(row,column) #finds the first tile + posititoin
            self.find_words()
            self.check_words()
            
        else:
            print("Word is not connected to another tile")
    def check_words(self):
        self.all_correct_words = True
        self.total_word_score = 0
        correct = self.check_straight_second()
        
        
        if correct == True:
            for i in self.word_list:
                print(i.piece)
                if i.piece not in game.dictionary_set:
                    print(f"{i.piece} is not a word")
                    self.all_correct_words = False
            if self.all_correct_words == True:

                for i in self.word_list:
                    self.total_word_score += i.value
                    
                    print(i.piece,i.value)
                print("TOTAL WORD SCORE")

                print(self.total_word_score)
                game.user_board.word_score = self.total_word_score
                

    def find_words(self):
        self.word_list = []
        for i in self.left_tile_list:
            new_word = False
            word = ""
            word_score = 0
            found = False
            difference = -1
            temp_word_list = []
            temp_word_score_list = []
            while found == False:
                difference += 1
                
                if game.user_board.board[i.row][i.column+difference].piece != "None":
                    new_word = True
                if game.total_board.board[i.row][i.column+difference].piece != "None":
                    
                    temp_word_list.append(game.total_board.board[i.row][i.column+difference].piece)
                    #print(game.total_board.board[i.row][i.column+difference].piece,game.total_board.board[i.row][i.column+difference].value)
                    temp_word_score_list.append(game.total_board.board[i.row][i.column+difference].value)
                else:
                    found = True
            
            if new_word == True:
                for i,f in zip(temp_word_list,temp_word_score_list):
                    word += i
                    word_score += f
                    print(f"{i} - {f}")
                    
                
                temp_item = Piece(word,word_score)
                
                self.word_list.append(temp_item)
                #print(self.word_list)
        for i in self.up_tile_list:
            new_word = False
            word = ""
            word_score = 0
            found = False
            difference = -1
            temp_word_list = []
            temp_word_score_list = []
            while found == False:
                difference += 1
                
                if game.user_board.board[i.row+difference][i.column].piece != "None":
                    new_word = True
                if game.total_board.board[i.row+difference][i.column].piece != "None":
                    temp_word_list.append(game.total_board.board[i.row+difference][i.column].piece)
                    temp_word_score_list.append(game.total_board.board[i.row+difference][i.column].value)
                    
                else:
                    found = True
            if new_word == True:
                for i,f in zip(temp_word_list,temp_word_score_list):
                    word += i
                    word_score += f
                    print(f"{i} - {f}")
                temp_item = Piece(word,word_score)
                self.word_list.append(temp_item)

    def check_orientation(self,row,column):
        horizontal = False
        if column - 1 < 0 and game.total_board.board[row + 1][column].piece != "None":
            left_most = game.total_board.board[row][column]
            horizontal = True
            found = True
        elif row + 1 > 14 and game.total_board.board[row-1][column].piece != "None":
            horizontal = True
        elif game.total_board.board[row][column+1].piece != "None" or game.total_board.board[row][column-1].piece != "None":
            
            horizontal = True
        vertical = False
        if column - 1 < 0 and game.total_board.board[row][column+1].piece != "None":
            left_most = game.total_board.board[row][column]
            vertical = True
            found = True
        elif column + 1 > 14 and game.total_board.board[row][column-1].piece != "None":
            vertical = True
        
        if column - 1 < 0 and game.total_board.board[row][column+1].piece != "None":
            up_most = game.total_board.board[row][column+1]
            vertical = False
        elif game.total_board.board[row+1][column].piece != "None" or game.total_board.board[row-1][column].piece != "None":
            vertical = True
        else:
            vertical = False
        if horizontal == True:
            found = False
            difference = 0
            while found == False:
                difference -= 1
                #print("valid stuff")
                #print(game.total_board.board[row][column].piece,row,column)
                if column + difference <0:
                    difference += 1
                    temp_tile = game.total_board.board[row][column+difference+1]
                    self.left_tile = Piece_and_Position(temp_tile.piece,temp_tile.value,row,column+difference+1)
                    found = True
                elif game.total_board.board[row][column+difference].piece == "None":
                    temp_tile = game.total_board.board[row][column+difference+1]
                    self.left_tile = Piece_and_Position(temp_tile.piece,temp_tile.value,row,column+difference+1)
                    
                    found = True
                    #print("its true")
                    #print(found)
            #print(self.left_tile.piece)
            #print(self.left_tile_list)
            if self.left_tile_list == []:
                self.left_tile_list.append(self.left_tile)
            else:
                duplicate = False
                for i in self.left_tile_list:
                    if self.left_tile.row == i.row and self.left_tile.column == i.column:
                        duplicate = True
                if duplicate == False:     
                    self.left_tile_list.append(self.left_tile)
        if vertical == True:

            found = False
            difference = 0
            while found == False:
                difference -= 1
                #print("valid stuff")
                #print(game.total_board.board[row][column].piece,row,column)
                if row + difference <0:
                    difference += 1
                    temp_tile = game.total_board.board[row+difference+1][column]
                    self.up_tile = Piece_and_Position(temp_tile.piece,temp_tile.value,row+difference+1,column)
                    found = True
                elif game.total_board.board[row+difference][column].piece == "None":
                    temp_tile = game.total_board.board[row+difference+1][column]
                    self.up_tile = Piece_and_Position(temp_tile.piece,temp_tile.value,row+difference+1,column)
                    
                    found = True
                    #print("its true")
                    #print(found)
            #print(self.left_tile.piece)
            #print(self.left_tile_list)
            if self.up_tile_list == []:
                self.up_tile_list.append(self.up_tile)
            else:
                duplicate = False
                for i in self.up_tile_list:
                    if self.up_tile.row == i.row and self.up_tile.column == i.column:
                        duplicate = True
                if duplicate == False:     
                    self.up_tile_list.append(self.up_tile)
                    
        
    def check_connected(self):
        self.connected = False
        for row in range(len(game.user_board.board)):
            for column in range(len(game.user_board.board[row])):
                if game.user_board.board[row][column].piece != "None":
                    
                    for difference in range(-1,2,2):
                        try:
                            if game.perm_board.board[row+difference][column].piece != "None":
                                self.connected = True
                            elif game.perm_board.board[row][column+difference].piece != "None":
                                self.connected = True
                        except:
                            pass
        if self.connected == True:                
            for row in range(len(game.user_board.board)):
                for column in range(len(game.user_board.board[row])):
                    if game.user_board.board[row][column].piece != "None":
                        temp_connected = False
                        for difference in range(-1,2,2):
                            if game.total_board.board[row+difference][column].piece != "None":
                                temp_connected = True
                            elif game.total_board.board[row][column+difference].piece != "None":
                                temp_connected = True 
                        if temp_connected == False:
                            self.connected = False    
                                    
    def dupe_board(self):
        for row in range(len(game.total_board.board)):
            for column in range(len(game.total_board.board[row])):
                self.board[row][column] = game.total_board.board[row][column]


        
        
            
        
            
        
    def perform_move(self):
        
        
        game.input_value.perform_move_type()
            


class Piece_and_Position:
    def __init__(self,piece,value,row,column):
        self.piece = piece
        self.value = value
        self.row = row
        self.column = column
    
class Inputs:
    def __init__(self,is_submit = None,move_type = None,pass_over_middle = None):
        self.is_submit = False
        self.move_type = move_type
        if pass_over_middle == None:
            self.pass_over_middle = False
        else:
            self.pass_over_middle = pass_over_middle
    def ask_move_type(self):
        move_type_valid = False
        while move_type_valid == False:
            move_type = input("What move type do you want? \n Enter 1 to move a tile on your rack to the board \n Enter 2 to move a tile on the rack to a different square on the rack\n Enter 3 to move a tile on the board to a different square on the board\n Enter 4 to move a tile on the board to a position on your rack\n Enter 'S' to submit your word\n Enter 'I' to see information\n Enter 'R' to replace some tiles on your rack\n")
            if move_type not in ['1','2','3','4'] and move_type.upper() not in ['S','I','R']:
                
                import os    
                os.system('cls' if os.name == 'nt' else 'clear')
                game.total_board.display_board()
                game.player_tiles.display_tiles(game.info.player_turn)
                print("Move type invalid, please enter a valid input")
            else:
                if move_type.upper() == "S" and game.user_board.valid_output == False:
                    if game.user_board.pass_over_middle == False:
                        print("First word must pass over H8")
                    else:
                        print("Word invalid, cannot submit, please enter a valid input")
                elif move_type.upper() == "I":
                    for i in range(len(game.info.player_scores)):
                        print(f"Player {i+1}'s score - {game.info.player_scores[i]}")
                #elif move_type.upper() == "R":
                    
                else:
                    #print("reutrned")
                    move_type_valid = True
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
                
                    if origin[0].upper() not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"] or origin[1:] not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
                        print("Not a valid position, please enter a letter A-P followed by a number 1-15 e.g(D13)")
                        origin = input("Enter the position where you want to draw your tile from: ")
                    else:
                        valid_move = True
                else:
                    print("Not a valid position, please enter a letter A-P followed by a number 1-15 e.g(D13)")
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
                
                    if destination[0].upper() not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"] or destination[1:] not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
                        
                        print("Not a valid position, please enter a letter A-P followed by a number 1-15 e.g(D13)")
                        destination = input("Enter the position where you want to place your tile: ")
                    else:
                        valid_move = True
                else:
                    print("Not a valid position, please enter a letter A-P followed by a number 1-15 e.g(D13)")
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
        self.move_type = self.ask_move_type()
        
        if self.move_type.upper() != "S" and self.move_type.upper() != "I" and self.move_type.upper() != "R":
            self.submitted = False
            origin = self.get_origin(self.move_type)
            destination = self.get_desintation(self.move_type)
            self.update_board(origin,destination)
            while self.submitted == False:
                self.move_type = self.ask_move_type()
                if self.move_type.upper() != "S" and self.move_type.upper() != "I" and self.move_type.upper() != "R":
                    origin = self.get_origin(self.move_type)
                    destination = self.get_desintation(self.move_type)
                    
                    self.update_board(origin,destination)
                elif self.move_type.upper() == "S":
                    self.submit(game.user_board.word_score)
                    self.submitted = True
                elif self.move_type.upper() == "R":
                    empty_board = True
                    for row in game.user_board.board:
                        for tile in row:
                            if tile.piece != "None":
                                empty_board = False
                    if empty_board == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("You cannot replace your tiles while you still have tiles on the board")
                    else:
                        game.input_value.ask_replace_tiles()
                        game.player_tiles.replace_tiles()
                        self.submitted = True
        
        elif self.move_type.upper() == "S":
            self.submit(game.user_board.word_score)
            self.submitted = True
        elif self.move_type.upper() == "R":
            empty_board = True
            for row in game.user_board.board:
                for tile in row:
                    if tile.piece != "None":
                        empty_board = False
            if empty_board == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You cannot replace your tiles while you still have tiles on the board")
            else:
                game.input_value.ask_replace_tiles()
                game.player_tiles.replace_tiles()
                self.submitted = True

    
                game.player_tiles.replace_tiles()
                self.is_submit = True
                self.submitted = True
    def submit(self,word_score):
        self.is_submit = False
        if game.user_board.valid_output == True:
            print("Word submitted")
            print(word_score)
            game.info.player_scores[game.info.player_turn] += word_score
            print(f"Player {game.info.player_turn+1}'s score - {game.info.player_scores[game.info.player_turn]}")
            self.is_submit = True
            
        else:
            print("Not a valid word")
        game.first_turn = False


    def update_board(self,origin,destination):
        
        
        if self.move_type == "1":
            tile = game.player_tiles.player_tiles[game.info.player_turn][int(origin) - 1]
            row_num = int(destination[1:]) - 1
            column_num = destination[0]
            column_num = ord(column_num.upper()) - 65
            if tile.piece == "None":
                print("You cannot move an empty tile.")
                self.submitted = False
            elif game.total_board.board[row_num][column_num].piece != "None":
                print("You cannot move a tile onto another tile.")
                self.submitted = False
            else:
                self.submitted = True
                game.player_tiles.player_tiles[game.info.player_turn][int(origin) - 1] = EmptyPiece()
                print(f"Tile {tile.piece} moved from {origin} to {destination.upper()}.")
                game.user_board.board[row_num][column_num] = tile
        elif self.move_type == "2":
            tile = game.player_tiles.player_tiles[game.info.player_turn][int(origin) - 1]
            tile2 = game.player_tiles.player_tiles[game.info.player_turn][int(destination) - 1] 
            game.player_tiles.player_tiles[game.info.player_turn][int(origin) - 1] = tile2
            game.player_tiles.player_tiles[game.info.player_turn][int(destination) - 1] = tile
            self.submitted = True
        elif self.move_type == "3":
            row_num = int(origin[1:]) - 1
            column_num = origin[0]
            column_num = ord(column_num.upper()) - 65
            destination_column = ord(destination[0].upper())-65
            #print('AIHSODFHASODFHO')
            #print(game.user_board.temp_board)
            tile = "None"
            for i in game.user_board.temp_board:
                #print(i.row,i.column,row_num,column_num)
                if i.row == row_num and i.column == column_num:
                    tile = i
            if tile == "None":
            
                print("You cannot move an empty tile.")
                self.submitted = False
            elif game.total_board.board[int(destination[1:])-1][destination_column].piece != "None":
                print("You cannot move a tile onto another tile.")
                self.submitted = False
            else:
                game.user_board.board[row_num][column_num] = EmptyPiece()
                
                self.submitted = True
            
                game.user_board.board[int(destination[1:])-1][destination_column] = tile
                print(f"Tile {tile.piece} moved from {origin} to {destination.upper()}.")
        elif self.move_type == "4":
            row_num = int(origin[1:]) - 1
            column_num = origin[0]
            column_num = ord(column_num.upper()) - 65
            tile = "None"
            for i in game.user_board.temp_board:
                #print(i.row,i.column,row_num,column_num)
                if i.row == row_num and i.column == column_num:
                    tile = i
            if tile == "None":
                print("You cannot move an empty tile.")
                self.submitted = False
            elif game.player_tiles.player_tiles[game.info.player_turn][int(destination)-1].piece != "None":
                print("You cannot move a tile onto a tile.")
                self.submitted = False
            else:
                game.user_board.board[row_num][column_num] = EmptyPiece()
                game.player_tiles.player_tiles[game.info.player_turn][int(destination)-1] = tile
                print(f"Tile {tile.piece} moved from {origin} to {destination.upper()}.")
                self.submitted = True
    def ask_replace_tiles(self):
        
        
        finished = False
        self.replace_tile_list = []
        
        while finished == False:
            position = input("What space do you want to replace? (Enter an empty space to finish)")
            if position not in ['1','2','3','4','5','6','7']:
                finished = True
            elif int(position) in self.replace_tile_list:
                print("You have already inputted this position")
            else:
                position = int(position)
                self.replace_tile_list.append(position)
            print(self.replace_tile_list)
        
      
        
            

        
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
    def refresh_tiles(self,tile_list):
        player_tiles = self.player_tiles
        #print(game.info.player_turn)
        for i in range(len(player_tiles[game.info.player_turn])):
            if player_tiles[game.info.player_turn][i].piece == "None":
                tile_list, random_tile = self.random_tile(tile_list)
                player_tiles[game.info.player_turn][i] = random_tile
                print(f"{random_tile.piece} drawn")
                
        return player_tiles, tile_list
    def replace_tiles(self):
        
        
        for i in game.input_value.replace_tile_list:
            game.player_tiles.tile_list, random_tile = game.player_tiles.random_tile(game.player_tiles.tile_list)
            game.player_tiles.player_tiles[game.info.player_turn][i-1] = random_tile
            print(f"{random_tile.piece} drawn")
        

class Information:
    def __init__(self,player_turn = None,player_scores = None):
        if player_turn == None:
            self.player_turn = 0
        else:
            self.player_turn = player_turn
        if player_scores == None:
            self.player_scores = []
            valid_num_players = False
            while valid_num_players == False:
                
                try:
                    self.num_players = int(input("How many players are playing?"))
                    if self.num_players < 2 or self.num_players > 4:
                        print("Please enter a number between 2 and 4")
                    else:
                        valid_num_players = True
                except:
                    print("Please enter a number between 2 and 4")
            for i in range(self.num_players):
                self.player_scores.append(0)
        else:
            self.player_scores = player_scores
    
                

class Main:
    def __init__(self,info = None,user_board = None,perm_board = None, player_tiles = None,dictionary_set = None,input_value = None,total_board = None,game_finished = None,first_turn = None):
        if info == None:
            self.info = Information()
        else:
            self.info = info
        if user_board == None:
            self.user_board = Board()   
        else:
            self.user_board = user_board
        if perm_board == None:
            self.perm_board = Board()
        else:
            self.perm_board = perm_board
        
        if dictionary_set == None:
            self.dictionary_set= set(line.strip() for line in open('dictionary.txt'))
        else:
            self.dictionary_set = dictionary_set
        if input_value == None:
            self.input_value = Inputs()
        else:
            self.input_value = input_value
        if total_board == None:
            self.total_board = Board()
        else:
            self.total_board = total_board
        if player_tiles == None:
            self.player_tiles = Tiles(0,self.info.num_players)
        else:
            self.player_tiles = player_tiles
        if game_finished == None:
            self.game_finished = False
        else:
            self.game_finished = game_finished
        if first_turn == None:
            self.first_turn = True
        else:
            self.first_turn = first_turn
        
    def player_move(self):    
        if game.total_board.board[7][7].piece == "None":
            game.user_board.pass_over_middle = False
        else:
            game.user_board.pass_over_middle = True
        
        self.user_board.perform_move()
        game.total_board.mix()
        
        
        #print(game.input_value.move_type)
        if game.input_value.move_type.upper() != "S" and game.input_value.move_type.upper() != "R":
            
            self.total_board.display_board()
            self.player_tiles.display_tiles(self.info.player_turn)
        if self.first_turn == True:
            self.user_board.check_straight()
        else:
            self.user_board.check_valid()
       
        
    def first_turn(self):
        if game.total_board.board[7][7].piece == "None":
            game.user_board.pass_over_middle = False
        else:
            game.user_board.pass_over_middle = True
        game.input_value.is_submit = False
        
        print(f"Player {game.info.player_turn +1}'s Turn!")
        
        
        self.total_board.display_board()
        
        self.player_tiles.display_tiles(self.info.player_turn)
        while game.input_value.is_submit != True:
            self.user_board.perform_move()
            game.total_board.mix()
            
            

            if game.input_value.move_type.upper() != "S" and game.input_value.move_type.upper() != "R":
                
                self.total_board.display_board()
                self.player_tiles.display_tiles(self.info.player_turn)
                self.user_board.check_straight()

            else:
                game.player_tiles.player_tiles, game.player_tiles.tile_list = game.player_tiles.refresh_tiles(game.player_tiles.tile_list)
                self.player_tiles.display_tiles(self.info.player_turn)

                temp_input = input("Enter any key to continue")
                game.perm_board.dupe_board()
                
                game.user_board = Board()
                game.info.player_turn += 1
                game.input_value.is_submit = True
    def player_turn(self):
        game.input_value.is_submit = False
        game.info.player_turn = game.info.player_turn % game.info.num_players
        print(f"Player {game.info.player_turn +1}'s Turn!")
        
        
        self.total_board.display_board()
        
        self.player_tiles.display_tiles(self.info.player_turn)
        while game.input_value.is_submit != True:
            game.player_move()
        else:
            print(game.info.player_turn)
            game.player_tiles.player_tiles, game.player_tiles.tile_list = game.player_tiles.refresh_tiles(game.player_tiles.tile_list)
            self.player_tiles.display_tiles(game.info.player_turn)
            if self.info.player_scores[self.info.player_turn] >= 100 :
                print(f"Player {game.info.player_turn} has won! They reached 100 points first.")
                self.game_finished = True
            temp_input = input("Enter any key to continue")
            game.perm_board.dupe_board()
            #game.perm_board.display_board()
            game.user_board = Board()
            game.info.player_turn += 1
            
            game.input_value.is_submit = True
import os        
game = Main()

os.system('cls' if os.name == 'nt' else 'clear')
while game.game_finished == False:
    
    game.player_turn()
    os.system('cls' if os.name == 'nt' else 'clear')
