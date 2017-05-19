'''
    Let's Play Some Tic Tac Toe!
    
    adg       ae       afh
    
    bd       begh       bf
    
    cdh       ce       cfg
    '''





def display(board):
    # displays the current board next to the board layout
    print("\033c")
    print()
    print(" WELCOME TO SUPER FUN TIC TAC TOE TIME! ")
    print()
    print()
    print("     CURRENT BOARD:          BOARD LAYOUT:")
    print()
    print("       {}  |  {}  |  {}          1  |  2  |  3  ".format(board[0][0], board[0][1], board[0][2]))
    print("     -----------------       -----------------")
    print("       {}  |  {}  |  {}          4  |  5  |  6  ".format(board[1][0], board[1][1], board[1][2]))
    print("     -----------------       -----------------")
    print("       {}  |  {}  |  {}          7  |  8  |  9  ".format(board[2][0], board[2][1], board[2][2]))
    print()
    print()




def move(board):
    # converts from the player's input to array indices
    code = {1: (0,0) , 2: (1, 0) , 3: (2, 0) ,
            4: (0,1) , 5: (1, 1) , 6: (2, 1) ,
            7: (0,2) , 8: (1, 2) , 9: (2, 2) }
    
    # selects the player and their token
    if board[3]==1:
        player = "1"
        token = "X"
        board[3] = 2
    else:
        player = "2"
        token = "O"
        board[3] = 1

    # asks the player for their move
    move = input("PLAYER " + player + " (" + token + "), Where would you like to place a piece? ")


    # checks that the move is legit
    if (not move.isdigit() or int(move) > 9 or move in board[4]):
        print("\nI'm sorry, that's not a legal move")
        input("You forfeit your turn (Press ENTER to continue)")
        return board

    # finds the row and column
    row = code[int(move)][1]
    column = code[int(move)][0]

    # places the player's token on the board and updates the tracking dictionary
    board[row][column] = token
    board[4][move] = token

    #checks if the player won
    if win(board):
        board[5] = True

    return board




def win(board):
    # check horizontal and vertical:
    for x in [0, 1, 2]:
        if (board[x][0] == board[x][1] == board[x][2] != " "
            or board[0][x] == board[1][x] == board[2][x] != " "):
            return True

    # check diagonals
    if (board[0][0] == board[1][1] == board[2][2] and board[1][1] != " "
        or board[2][0] == board[1][1] == board[0][2] and board[1][1] != " "):
        return True

    # no luck?
    return False

#   my original code checked fewer rows/columns, but needed to know the
#    if (board[row][0] == board[row][1] == board[row][2]
#        or board[0][column] == board[1][column] == board[2][column]
#        or board[0][0] == board[1][1] == board[2][2] and board[1][1] != " "
#        or board[2][0] == board[1][1] == board[0][2] and board[1][1] != " "):
#        return True
#    else:
#        return False




if __name__ == "__main__":
    
    # board[3] is the current player, board[4] keeps track of what spots have been played, board[5] is if someone won
    board =    [ [" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "],
                 1, {}, False ]

    while len(board[4]) < 9:
        display(board)          # show the board
        board = move(board)     # make a move
        if board[5] == True:    # did I win yet?
            break        #       then let's leave this loop!

    display(board)

    if len(board[4]) == 9:
        print("Tie\n")
        input("Press ENTER to continue: ")
    else:
        print("Great Job, PLAYER {}, You Won the Game!\n".format(board[3]))
        input("Press ENTER to continue: ")
    print("\033c")





