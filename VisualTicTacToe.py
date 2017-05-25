import pygame
from pygame.locals import *
import random
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~ DISPLAY THE BOARD ~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
def display(board):

    screen.fill(0)                          # clears the screen

    screen.blit(gameboard,(0,0))            # display background
    for x in range(0,3):                    # display pieces
        for y in range(0,3):
            if board[y][x]==True:
                screen.blit(xes,(start_x+x*cell_width,start_y+y*cell_width))
            elif board[y][x]==False:
                screen.blit(oes,(start_x+x*cell_width,start_y+y*cell_width))

    pygame.display.update()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ PLAYER 2 -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
def player2(board):
    code = { 1: (0,0), 2: (1, 0), 3: (2, 0),
             4: (0,1), 5: (1, 1), 6: (2, 1),
             7: (0,2), 8: (1, 2), 9: (2, 2) }

    if board[4] == 1:                                 # human opponent
        move = player1(board)
        return move


    if board[4] == 2:                                 # Stupid Computer
        index = random.randint(0,len(board[3])-1)
        return board[3][index]
    

    if board[4] == 3:                                 # Smart Computer
        # check first for winning moves
        for x in board[3]:
            row = code[int(x)][1]
            column = code[int(x)][0]
            
            board2 = []
            for i in range(0, 3):
                board2 += [board[i][:]]
            
            board2[row][column] = False

            if win(board2):
                return x

        # then check if the opponent can win
        for x in board[3]:
            row = code[int(x)][1]
            column = code[int(x)][0]
            board2 = []
            for i in range(0, 3):
                board2 += [board[i][:]]
            board2[row][column] = True

            if win(board2):
                return x

        # if no one is set to win, return a random number
        index = random.randint(0,len(board[3])-1)
        return board[3][index]


# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ PLAYER 1 -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
def player1(board):
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                y = (position[1]-start_y)//cell_width
                x = (position[0]-start_x)//cell_width
                move = (x+1) + 3*(y)
                if (move not in board[3]):
                    move = player1(board)
                return move

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ EACH MOVE ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
def turn(board):
    # converts from the player's input to array indices
    code = { 1: (0,0), 2: (1, 0), 3: (2, 0),
             4: (0,1), 5: (1, 1), 6: (2, 1),
             7: (0,2), 8: (1, 2), 9: (2, 2) }
    
    # selects the player and their token
    
    if board[5]:
        move = player1(board)
    else:
        move = player2(board)

    # finds the row and column
    row = code[int(move)][1]
    column = code[int(move)][0]

    # places the player's token on the board and updates the tracking dictionary
    board[row][column] = board[5]
    board[3].remove(int(move))

    #checks if the player won
    if win(board):
        board[6] = True

    board[5] = not board[5]

    return board

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ CHECK FOR WIN ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #

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


# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~ WHAT TYPE OF GAME? -~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
def choice():
    screen.fill(0)

    screen.blit(options,(0,0))
#    screen.blit(pretty, (37,152))
#
#    start_x = 37
#    start_y = 82
#    height = 70

    one = 82
    two = 152
    three = 222
    four = 292
    
    pygame.display.update()
    wait = 0
    while wait == 0:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                
                if position[0] > 37:        # correctly positioned in x-dimenstion
                    if (position[1] > one and position[1] < two):
                        return 1
                    if (position[1] > two and position[1] < three):
                        return 2
                    if (position[1] > three and position[1] < four):
                        return 3
                    if (position[1] > four):
                        return 4




# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ STARTING POINT -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #
# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ #


if __name__ == "__main__":
    pygame.init()
    
    width, height = 375, 375
    screen=pygame.display.set_mode((width, height))
    
    start_x = start_y = 58
    cell_width = 93
    
    pretty = pygame.image.load("resources/pretty.png")
    gameboard = pygame.image.load("resources/gameboard.png")
    options = pygame.image.load("resources/options.png")
    xes = pygame.image.load("resources/x.png")
    oes = pygame.image.load("resources/o.png")
    player2win = pygame.image.load("resources/player2win.png")
    player1win = pygame.image.load("resources/player1win.png")
    computerwin = pygame.image.load("resources/computerwin.png")
    tiegame = pygame.image.load("resources/tie.png")

    while True:                         # all-encompasing program. only way out is to quit.
    
        board =  [ [" ", " ", " "],     # [0,2] To keep track of where tokens are placed
                   [" ", " ", " "],
                   [" ", " ", " "],
                   [1,    2,   3,       # [3] To keep track of what spaces are empty
                    4,    5,   6,
                    7,    8,   9],
                    0,                  # [4] To keep track of the current game
                                        #   1 = human vs human
                                        #   2 = human vs dumb computer
                                        #   3 = human vs smart computer
                                        #   4 = quit
                    True,               # [5] To keep track of the current player
                                        #    True = player 1
                                        #    False = player 1 (or computer)
                    False,      ]       # [6] Has anyone won?
                                        #    True = there is a winner
                                        #    False = there is no winner

                
        board[4] = choice()             # Select the game
        if board[4] == 4:
            pygame.quit()
            exit(0)
        
        while len(board[3]) > 0:
            display(board)          # show the board
            board = turn(board)     # make a move
            if board[6]:            # did anyone win yet?
                break               #       then let's leave this loop!


        # LAST VIEW TO AVOID CONFUSION
        screen.fill(0)                          # clears the screen
        display(board)
        
        
        font = pygame.font.Font(None, 48)
        gameover = font.render("GAME OVER", True, (0,0,0))
        textRect = gameover.get_rect()
        textRect.topleft = [80, 10]
        screen.blit(gameover, textRect)
        
        font = pygame.font.Font(None, 40)
        results = font.render("Click for results", True, (0,0,0))
        textRect = results.get_rect()
        textRect.topleft = [80, 320]
        screen.blit(results, textRect)
        
        pygame.display.update()
        wait = 0
        while wait == 0:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    wait = 1



        # VICTORY SCREEN
        screen.fill(0)                          # clears the screen
        if not board[6]:                        # no win, so it's a tie
            screen.blit(tiegame,(0,0))
        elif board[5]:                          # player 2 wins
            if board[4] == 1:
                screen.blit(player2win,(0,0))   # player 2 is a person
            else:
                screen.blit(computerwin, (0,0)) # player 2 is a computer
        else:
            screen.blit(player1win,(0,0))       # player 1 wins
        pygame.display.update()
        wait = 0
        while wait == 0:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    wait = 1

#



