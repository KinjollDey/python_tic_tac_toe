## Tic tac toe using pythom

#----------------GLOBAL VARIABLES-------------------

## Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"] ## Storing the board as a list

## IF game is still going
game_on = True

## Winner
winner = None

## Which Player's Turn
current_player = "X" #(Considering X Goes First)

#-------------------------------------FUNCTIONS-----------------------------
## Run the game
def play(): 
    ## Display Current board
    display_board()

## Loop as long as the game is going on
    while game_on:

## Taking Player's input 
        players_choice(current_player)

## Check Win/tie
        check_if_game_over()

## Flip to other player
        flip_player()
    
## Winner prompt
    if winner == "X" or winner == "O":
        print(winner + " won the game.")
        print("Hurrahh")
    elif winner == None:
        print("Its a tie")

# Display board
# Creating a function to display board at will
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")



## Handle user input in a single turn
def players_choice(player): ## Since we are giving Current_plaer Argument in play()
   
    print(player + "'s turn.")

    position = input("Choose a position from 1 to 9 going row-wise:")
    
    ## Make sure the input is valid and not overwriting:

    valid = False
    while not valid:

        ## Make sure input is valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9" ]:
            position = input("Choose a position from 1 to 9 going row-wise:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Invalid Input, Try again.")

    ## Input in board
    board[position] = player
    display_board()

## To check if there's a win or a tie
def check_if_game_over():
    check_if_win() 
    check_if_tie()

## Checking for win of either player    
def check_if_win():
    ## Set up global variables
    global winner
    ## Check if there's a winner. 
    ## Check rows
    row_winner = check_rows()
    ## check coloums
    column_winner = check_coloums()
    ## check diagonals
    diag_winner = check_diags()
    ## Getting the winner:
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None

## Checks rows for win
def check_rows():
    ## Set Global Variable
    global game_on 
    ## Check for match acc to game
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    ## If any one row has a match??
    if row_1 or row_2 or row_3:
        game_on = False
    ## for Winner:
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_coloums():
    ## Set Global Variable
    global game_on 

    ## Check for match acc to game
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    ## If any one row has a match??
    if column_1 or column_2 or column_3:
        game_on = False
    
    ## for Winner:
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
    
def check_diags():
    ## Set Global Variable
    global game_on 

    ## Check for match acc to game
    diags_1 = board[0] == board[4] == board[8] != "-"
    diags_2 = board[2] == board[4] == board[6] != "-"

    ## If any one row has a match??
    if diags_1 or diags_2:
        game_on = False
    
    ## for Winner:
    if diags_1:
        return board[0]
    elif diags_2:
        return board[2]
    else:
        return None

## Check tie
def check_if_tie():
    #Global
    global game_on
    
    if "-" not in board:
        game_on = False 
    return

## change Turns
def flip_player():
    ## Global Variable
    global current_player
## Switch fron X to O player
    if current_player == "X":
        current_player = "O"
## Switch from O to X player        
    elif current_player == "O":
        current_player = "X"


#---------------------PLAY GAME----------------------
play()









