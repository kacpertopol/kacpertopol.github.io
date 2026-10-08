import sys

state = {"iterator" : 0 , "finished" : False , "points" : 0}

# If the file "state" exists in directory:
# "/some/path/on/your/computer/with/the/state"
# (please replace this with an appropriate path)
# load the state using your implementation of "readState":
#    state = readState("/some/path/on/your/computer/with/the/state")
# 
# Hint, import the "os" module:
#    import os
# then check if the file exists using:
#    os.path.isfile("/some/path/on/your/computer/with/the/state")

def updateGameState(s):
    r = input("Ile wynosi 1 + 1? ")

    if(int(r) == 2):
        state["points"] += 1
        print("BRAWO!!!!!")
    else:
        print("NA PEWNO? PROSZĘ SPRÓBOWAĆ JESZCZE RAZ.")
        r1 = input("Ile wynosi 1 + 1? ")
        if(int(r1) == 2):
            print("NO, UDAŁO SIĘ!")
            state["points"] += 1
        elif(int(r1) < 0):
            print("ZAPLĄTAŁ SIĘ ZNAK -, PROSZĘ SPRÓBOWAĆ JESZCZE RAZ.")
            r2 = input("Ile wynosi 1 + 1? ")
            if(int(r2) == 2):
                print("W KOŃCU!!")
                state["points"] +=1
        else:
            print("COŚ KIEPSKO Z ARYTMETYKĄ!")

    s["iterator"] += 1
    if(s["iterator"] == 10):
        s["finished"] = True

def myPixel(i , j):
    if(i == 79):
        sys.stdout.write("x\n")
    else:
        sys.stdout.write("x")
    return "x"

def showGameState(s):
    sys.stdout.write("AKTUALNA LICZBA PUNKTÓW: " + str(s["points"]) + "\n")
    pixels = [[myPixel(i , j) for i in range(80)] for j in range(20)]

while(not state["finished"]):
    updateGameState(state)
    showGameState(state)

# Write the state automatically to 
# "/some/path/on/your/computer/with/the/state"
# by using your implmentation of:
#    writeState(state , "/some/path/on/your/computer/with/the/state")
# or ask the user if he / she want's to save the progress. You can do this
# here or inside the "updateGameState" function.

# Example of writing to and reading from files are below.
# Be carefull not to accidentally overwrite 
# something important on your machine.

#with open("state" , "w") as f:
#    f.write(str(123) + "\n")
#    f.write(str(321) + "\n")

# Example of reading from file:
#with open("state" , "r") as f:
#    a = int(f.readline())
#    b = int(f.readline())
#    print(a + b)
     
