# sauce : https://www.pygame.org/docs/

# imports:
import numpy as np
from scipy.signal import convolve2d
import pygame

# set the max frame rate in frames / second: 
framerate = 60
# set the number of cels in row and column:
cells = 100
# each cell will be drawn as a pixels x pixels square region: 
pixels = 10

# change this to eg np.float64 if you want to implement a smooth version of the game:
celltype = np.int32 
# kernel for the classic game of life, change this if you want to implement a smooth version of the game:
kernel = np.array([[1 , 1 , 1] , [1 , 0 , 1] , [1 , 1 , 1]] , dtype = celltype)

# create a window:
display = pygame.display.set_mode((cells * pixels , cells * pixels))

# create a clock that will limit the number of frames per second (see clock.tick(framerate) below):
clock = pygame.time.Clock()

#################################################
# TODO:                                         # 
# INITIALIZE THE STATE OF THE GAME OF LIFE HERE #
#################################################

# state of the game
running = True
paused = True
single = None

# main loop of the program:
while(running):
    # handling events:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            # close window to quit
            running = False
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_p):
                # press p to pause, press p again to start
                paused = not paused
            elif(event.key == pygame.K_s):
                # press s for a single step
                single = True
                paused = False
            elif(event.key == pygame.K_r):
                # press r to load random cells into the state
                state = np.random.randint(0 , high = 2 , size = (cells , cells))

        elif(event.type == pygame.MOUSEBUTTONUP):
            # click right button to change state of cell:
            pos = pygame.mouse.get_pos()
            x , y = pos
            x , y , = int(x / pixels) % cells , int(y / pixels) % cells
            state[x , y] = (state[x , y] + 1) % 2

    # pygame expects a 
    #   cells * pixels by cells * pixels
    # array with values 0 ... 255, to get this from state:
    ########################################################################
    # TODO:                                                                #
    # THIS WORKS FOR THE CLASSIC GAME OF LIFE WHERE THE CELLS HAVE INTEGER #
    # VALUES, CHANGE THIS APPROPRIATELY IF YOU WANT A SMOOTH VERSION       #
    ########################################################################
    p = 255 * np.repeat(np.repeat(state , pixels , axis = 1) , pixels , axis = 0)

    # display p in the window:
    surf = pygame.surfarray.make_surface(p)
    display.blit(surf , (0 , 0))
    pygame.display.update()
    
    if(not paused):
        # the meat of the programm, the actual iterations of the game start here ...
        ####################################################################
        # TODO:                                                            #
        # THIS BIT OF CODE SHOULD IMPLEMENT A SINGLE ITERATION OF THE GAME #
        # AND UPDATE THE CELLS                                             #
        ####################################################################
        # ... end end here 

        if(single):
            single = False
            paused = True

    clock.tick(framerate)

pygame.quit()
