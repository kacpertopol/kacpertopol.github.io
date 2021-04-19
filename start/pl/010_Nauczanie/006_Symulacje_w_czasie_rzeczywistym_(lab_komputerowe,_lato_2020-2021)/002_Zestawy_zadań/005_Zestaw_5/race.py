#!/usr/bin/env python

import pygame
import argparse
import math

############################################################
#                                                          #
# change updateState to change the behaviour of the "worm" #
#                                                          #
############################################################


#def updateState(oldState , deltaT , inpt):
#    """
#    Arguments:
#        oldState -  (x , y , vx , vy , t , extra)
#                    x , y - position on the screen
#                    vx , vy - velocity
#                    t - time
#                    extra - internal state
#        deltaT -    time step
#        inpt -      list with characters that correspond 
#                    to pressed keys
#    Returns:
#        (x1 , y1 , vx1 , vy1 , t1 , extra1) - new state after time step
#    """
#    x , y , vx , vy , t , extra = oldState
#    ipt = extra
#    if("w" in inpt):
#        ipt = (ipt[0] , ipt[1] - 0.0001)
#    if("s" in inpt):
#        ipt = (ipt[0] , ipt[1] + 0.0001)
#    if("a" in inpt):
#        ipt = (ipt[0] - 0.0001 , ipt[1])
#    if("d" in inpt):
#        ipt = (ipt[0] + 0.0001 , ipt[1])
#    return (x + vx * deltaT , y + vy * deltaT , vx + ipt[0] * deltaT  , vy + ipt[1] * deltaT , t + deltaT , ipt)


def updateState(oldState , deltaT , inpt):
    """
    Arguments:
        oldState -  (x , y , vx , vy , t , extra)
                    x , y - position on the screen
                    vx , vy - velocity
                    t - time
                    extra - internal state
        deltaT -    time step
        inpt -      list with characters that correspond 
                    to pressed keys
    Returns:
        (x1 , y1 , vx1 , vy1 , t1 , extra1) - new state after time step
    """

    ## unpack the old state 

    x , y , vx , vy , t , extra = oldState

    ## handle user input

    ### by default the internal state of the worm does not change
    
    new_extra = extra

    ### the three possible states of the worm are:
    ### - "l" (I'm turning left)
    ### - "r" (I'm turning right)
    ### - "0" (I'm going streight)
    if("d" in inpt):
        new_extra = "l"
    if("a" in inpt):
        new_extra = "r"
    if("s" in inpt):
        new_extra = "0"
       
    ## calcualte the acceleration, the "warm" is supposed to move in
    ## circles so this is perpendicular to the velocity

    acc = (0.0 , 0.0)
    nrm = math.sqrt(vx * vx + vy * vy)
    if(new_extra == "l"):
        acc = (-(vy / nrm) * nrm * nrm / 60 , (vx / nrm) * nrm * nrm / 60)
    if(new_extra == "r"):
        acc = ((vy / nrm) * nrm * nrm / 60 , -(vx / nrm) * nrm * nrm / 60)

    ## very primitive metod of integration, can you can do better

    return (x + vx * deltaT , y + vy * deltaT , vx + acc[0] * deltaT  , vy + acc[1] * deltaT , t + deltaT , new_extra)


if(__name__ == "__main__"):

    # parsing command line arguments

    parser = argparse.ArgumentParser(description = "Simple racing game.")
    parser.add_argument("--resolution" , "-r" , help = "Resolution eg 640x480.")
    parser.add_argument("--capture" , "-c" , help = "Path to write captured input.")
    parser.add_argument("--track" , "-t" , help = "Path to write captured trace.")
    parser.add_argument("--draw" , "-d" , help = "Path to read captured trace.")
    parser.add_argument("--play" , "-p" , help = "Path to read captured input.")
    parser.add_argument("--initial" , "-i" , help = "Initial velocity.")
    parser.add_argument("--verbose" , "-v" , action = "store_true" , help = "Set verbose output.")
    args = parser.parse_args()
   
    # setting the resolution

    (width , height) = (500 , 500)
    if(args.resolution != None):
        width , height = map(int , args.resolution.split("x"))

    # reading captured input

    input_capture = []
    if(args.play != None):
        with open(args.play , "r") as f:
            ln = 0
            for line in f.readlines():
                if(ln == 0):
                    ## updating resolution
                    width , height = map(lambda x : int(x) , line.split())
                else:
                    spl = line.split()
                    tm = float(spl[0])
                    inp = spl[1].split("_")
                    input_capture.append((tm , inp))
                ln += 1
    
    # reading saved "worm" track

    track_compare = []
    if(args.draw != None):
        with open(args.draw , "r") as f:
            for line in f.readlines():
                track_compare.append(list(map(lambda x : float(x) , line.split())))

    # list for captured states

    track_capture = []

    # screen center

    centerx , centery = 0.5 * width , 0.5 * height

    # pygame initialization

    pygame.init()
    display = pygame.display.set_mode((width , height))
   
    # clock initialization
    clock = pygame.time.Clock()


    # initialize state
    x , y = centerx , centery 
    vx , vy = 0.0 , -0.2
    if(args.initial != None):
        vy = float(args.initial)
    t = 0.0
    extra = (0 , 0)
    
    # main game loop

    replay_index = 0
    finished = False
    ind = 0
    cen = [(x , y) for _ in range(20)]
    rad = [10 for _ in range(20)]
    frame = 0
    while(not finished):
        clock.tick(60)
        delta = clock.get_time()
        ev = []

        ## handle keyboard events or reading captured input

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                finished = True
            elif(event.type == pygame.KEYDOWN):
                if(args.play == None):
                    if(event.key == pygame.K_w):
                        ev.append("w")
                    if(event.key == pygame.K_s):
                        ev.append("s")
                    if(event.key == pygame.K_a):
                        ev.append("a")
                    if(event.key == pygame.K_d):
                        ev.append("d")
        if(args.play != None):
            if(len(input_capture) > 0):
                if(replay_index < len(input_capture)):
                    if(t > input_capture[replay_index][0]):
                        ev = input_capture[replay_index][1]
                        if(args.verbose):
                            print("game time: " , t , "| input time: " , input_capture[replay_index][0] , "| input_value: " , input_capture[replay_index][1])
                        replay_index += 1

        ## draw the "worm"

        ind = frame % 10
        cen[ind] = (x , y)
        rad[ind] = 6 + int(5.5 * math.sin(2.0 * math.pi * pygame.time.get_ticks() / 1000.0))

        display.fill((0 , 0 , 0))

        for line in track_compare:
            pygame.draw.circle(display , (255 , 0 , 0) , ((int(line[0]) , int(line[1]))) , 2)

        for i in range(10):
            pygame.draw.circle(display , (255 , 255 , 255), cen[i] , rad[i])

        frame += 1

        ## update the state of the "worm"

        x , y , vx , vy , tt , extra = updateState((x , y , vx , vy , t , extra) , delta , ev)
        
        ## we are ignoring tt and updating the time separately
        t = t + delta
        
        ## save input
        
        if(ev != [] and args.play == None):
            input_capture.append((t , ev))

        ## update pygame display

        pygame.display.update()
       
        ## we are assuming periodic boundries

        x = x%width
        y = y%height

        ## save the current state

        track_capture.append((x , y , vx , vy , t , extra))
      
    # save captured user input

    if(args.capture != None):
        with open(args.capture , "w") as f:
            f.write(str(width) + " " + str(height) + "\n")
            for line in input_capture:
                f.write(str(line[0]) + " " + "_".join(line[1]) + "\n")

    # save the captured "worm" states

    if(args.track != None):
        with open(args.track , "w") as f:
            for line in track_capture:
                f.write(" ".join(list(map(lambda x : str(x) , line[0:-1]))) + "\n")

