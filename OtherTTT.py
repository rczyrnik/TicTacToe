'''
    Significant help from https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
    Modified for my goals
    
    move and fire with arrow keys
    '''

# 1 - Import library
import pygame
import math
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
playerpos=[width//2-22,height-45]
invaders=[[30,10],[130,10],[230,10],[330,10],[430,10],[530,10]]
#invaders=[[30,10],[130,10],[230,10],[330,10],[430,10],[530,10]]
#invaders=[[30,10],[80,10],[130,10],[180,10],[230,10],[280,10],[330,10],[380,10],[430,10],[480,10],[530,10],[580,10]]
#n = 6
#invaders = []
#for x in range(0, n):
#    invaders += [[x*width//n, 10]]
#print(invaders)
left = True
down = False
acc=[0,0]
bullets=[]
GameTime = 90000
healthvalue = 194
step = 0

# 3 - Load images
player = pygame.image.load("resources/defense.png")
space = pygame.image.load("resources/space.png").convert()
ground = pygame.image.load("resources/ground.png").convert()
invaderimg = pygame.image.load("resources/invader.png")
invaderimg2 = pygame.image.load("resources/invader2.png")
bulletimg = pygame.image.load("resources/bullet.png").convert()
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")

# 4 - keep looping through
running = True
while running:
    # Stop when time runs out
    if (GameTime-pygame.time.get_ticks())//1000 == 0:
        running = False
    
    # Draw Background
    screen.fill(0)                                      # clears the screen
    
    for x in range(width//space.get_width()+1):         # background
        for y in range(height//space.get_height()+1):
            screen.blit(space,(x*300,y*300))
    
    for x in range(width//ground.get_width()+1):        # planet
        screen.blit(ground,(x*300,height-40))


    # Place and Draw Invaders

    for invader in invaders:
        if invader[0]%100 == 60:
            left = False
            down = True
        
        if invader[0]%100 == 0:
            left = True
            down = True
        # move left or right each round
        if left == True:
            invader[0]+=1
        else:
            invader[0]-=1



        if down == True:
            invader[1]+=30
            down = False


        # remove invader that reached the bottom
        if invader[1] > (height-80):
            invaders.pop(index)

        # draw invader
        badrect = pygame.Rect(invaderimg.get_rect())
        badrect.top = invader[1]
        badrect.left = invader[0]
        screen.blit(invaderimg, invader)


    # 6.2 - Draw bullet
    for bullet in bullets:
        index=0
        velocity = 3
        bullet[1]-=velocity
#        if bullet[0]<0:
#            bullets.pop(index)
#            playerpos[0] += 100     # doesn't seem to be working :(
        index+=1
        screen.blit(pygame.transform.rotate(bulletimg, 0), (bullet[0], bullet[1]))

    # 6.1 - Draw player
    screen.blit(player, playerpos)

    # 6.3.2 - Check for collisions
    for bullet in bullets:
        bullrect=pygame.Rect(bulletimg.get_rect())
        bullrect.left=bullet[0]
        bullrect.top=bullet[1]

        for invader in invaders:
            badrect = pygame.Rect(invaderimg.get_rect())
            badrect.top = invader[1]
            badrect.left = invader[0]
            # this is backwards from before, suggeting that one is wrong.
            # but which one? we'll never know...

            if badrect.colliderect(bullrect):
                acc[0]+=1
                invaders.remove(invader)
                bullets.remove(bullet)

#        if badrect.left < 64:
#            hit.play()
#            healthvalue -= random.randint(5,20)
#            invaders.pop(index)

    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)

    survivedtext = font.render(str((GameTime-pygame.time.get_ticks())//1000).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,450]
    screen.blit(survivedtext, textRect)

#    # 6.5 - Draw health bar
#    screen.blit(healthbar, (5,450))
#    for health1 in range(healthvalue):
#        screen.blit(health, (health1+8,453))

    # 7 - update the screen
    pygame.display.update()

    # 8 - dealing with key presses
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            # not sure what this does, but looks important
            pygame.quit()
            exit(0)
        
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                # fires a bullet
                acc[1]+=1
                bullets.append([playerpos[0]+19,playerpos[1]])
#                healthvalue -= 5
#                if healthvalue < 0:
#                    running = False
            if event.key==K_x:
                # quits the game
                pygame.quit()
                exit(0)
            if event.key==K_q:
                running = False

    # moving back and forth
    # treated differently, becasue can hold down key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: playerpos[0]-=5
    if keys[pygame.K_RIGHT]: playerpos[0]+=5


# game over time

screen.fill(0)                                      # clears the screen

for x in range(width//space.get_width()+1):         # background
    for y in range(height//space.get_height()+1):
        screen.blit(space,(x*300,y*300))

for x in range(width//ground.get_width()+1):        # planet
    screen.blit(ground,(x*300,height-40))

screen.blit(gameover, (450,405))



