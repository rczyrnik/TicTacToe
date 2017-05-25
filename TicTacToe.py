'''

    Let's Play Some Tic Tac Toe!

    '''
import random

def choice():
    
    print("\033c")
    print()
    print(" WELCOME TO SUPER FUN TIC TAC TOE TIME! ")
    print()
    print()
    print("     What sort of opponent would you like?")
    print()
    print("     1. Human player")
    print("     2. Random computer")
    print("     3. Marginally intelligent computer")
    print()
    print()
    my_choice = input("     (please choose a number) ")

    if  (not my_choice.isdigit() or int(my_choice) > 3):
        input("\nI'm sorry, I don't understand. Please select again. (Press ENTER to continue)" )
        choice()
        
    return my_choice

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

def itsawin(board):
    if board[6] != "1" and board[3]==1:
        print()
        print("     YOU GOT BEAT BY THE COMPUTER          ")
        print("                                           ")
        print("                                           ")
        print("            O        O                     ")
        print("                                           ")
        print("                |                          ")
        print("                                           ")
        print("                                           ")
        print("           /----------\                    ")
        print("                                           ")
        print("                                           ")
        print("       BETTER LUCK NEXT TIME               ")
        print("                                           ")
        print()
        return
    elif board[6] != "1":
        name = "HUMAN"
    else:
        if board[3]==1:
            name = "HUMAN PLAYER O"
        else:
            name = "HUMAN PLAYER X"

#    print("\033c")
    print()
    print("     CONGRATULATIONS {}          ".format(name))
    print("    __                                     ")
    print("   /  \                              __    ")
    print("   \__/       YOU WON THE GAME!     /  \   ")
    print("     \   __                         \__/   ")
    print("     /  /  \               __         \    ")
    print("    /   \__/              /  \        /    ")
    print("    \    /                \__/       /     ")
    print("         \                  \        \     ")
    print("         /                   \             ")
    print("                             /             ")
    print()


def player2(board):
    code = { 1: (0,0), 2: (1, 0), 3: (2, 0),
             4: (0,1), 5: (1, 1), 6: (2, 1),
             7: (0,2), 8: (1, 2), 9: (2, 2) }
    
    if board[6] == "1":                                 # human opponent
        # asks the player for their move
        move = input("PLAYER 2, where would you like to place a piece? ")

        # checks that the move is legit
        if (not move.isdigit() or int(move) > 9 or int(move) not in board[4]):
            input("Sorry, that's not a legal move, please try again. (Press ENTER to continue)")
            move = player2(board)

        return move


    if board[6] == "2":                                 # Stupid Computer
        index = random.randint(0,len(board[4])-1)
        return board[4][index]
    
    
    if board[6] == "3":                                 # Smart Computer
        # check first for winning moves
        for x in board[4]:
            row = code[int(x)][1]
            column = code[int(x)][0]
            board2 = []
            for i in range(0, 3):
                board2 += [board[i][:]]
            board2[row][column] = "O"

            if win(board2):
                return x

        # then check if the opponent can win
        for x in board[4]:
            row = code[int(x)][1]
            column = code[int(x)][0]
            board2 = []
            for i in range(0, 3):
                board2 += [board[i][:]]
            board2[row][column] = "X"

            if win(board2):
                itsawin(board)
                return x

        # if no one is set to win, return a random number
        index = random.randint(0,len(board[4])-1)
        return board[4][index]



def player1(board):
    # asks the player for their move
    move = input("PLAYER 1, where would you like to place a piece? ")

    # checks that the move is legit
    if (not move.isdigit() or int(move) > 9 or int(move) not in board[4]):
        print("\nSorry, that's not a legal move, please try again.\n")
        move = player1(board)

    return move

def move(board):
    # converts from the player's input to array indices
    code = { 1: (0,0), 2: (1, 0), 3: (2, 0),
             4: (0,1), 5: (1, 1), 6: (2, 1),
             7: (0,2), 8: (1, 2), 9: (2, 2) }
    
    # selects the player and their token
    if board[3]==1:
        token = "X"
        move = player1(board)
        board[3] = 2

    else:
        token = "O"
        move = player2(board)
        board[3] = 1


    # finds the row and column
    row = code[int(move)][1]
    column = code[int(move)][0]

    # places the player's token on the board and updates the tracking dictionary
    board[row][column] = token
    board[4].remove(int(move))

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





if __name__ == "__main__":
    
    # board[3] is the current player, board[4] keeps track of what spots have been played, board[5] is if someone won

    board =    [ [" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "],
                 1,
                 [1, 2, 3,
                  4, 5, 6,
                  7, 8, 9],
                 False,
                 0
                ]
    board[6] = choice()

    while len(board[4]) > 0:
        display(board)          # show the board
        board = move(board)     # make a move
        if board[5] == True:    # did I win yet?
            break               #       then let's leave this loop!

    display(board)

    if len(board[4]) == 0:
        print("It's a Tie!\n")
    else:
        itsawin(board)
    input("Press ENTER to continue: ")
    print("\033c")





