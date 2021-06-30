import time
import random
from tkinter import *

window = Tk()
window.title("Timer")
window.geometry("400x400")

def GenerateScramble():
    moves = [["F", "F'", "F2"], ["U", "U'", "U2"], ["R", "R'", "R2"], ["L", "L'", "L2"], ["D", "D'", "D2"], ["B", "B'", "B2"]]
    scramble = ""
    index = 6 
    for i in range(0, 20):
        notPrev = []
        for j in range(0,6):
            if not j == index:
                notPrev.append(j)
        index = notPrev[random.randint(0,4)]
        subList = moves[index]
        move = subList[random.randint(0,2)]
        scramble = scramble + move + " "
    return scramble


bigF = Frame(window)
bigF.grid()

f0 = Frame(bigF, width = 30)
f0.grid(row=0,column=0)
f1 = Frame(bigF, width = 30)
f1.grid(row=1,column=0)
f2 = Frame(bigF, width = 30)
f2.grid(row=2,column=0)
f3 = Frame(bigF, width = 30)
f3.grid(row=3,column=0)

scrambleL = Label(f0, text = GenerateScramble())
scrambleL.grid(row=0,column=0)

timerL = Label(f1, text = "15") # atm this is used for inspection
timerL.grid(row=0,column=0)

solveL = Label(f2, text = "0.0") # atm used for timer
solveL.grid(row=0,column=0)

timesT = Text(f3, height = 10, width = 13)
timesT.grid(row=0,column=0)

        

inspecting = False
timing = False

# inspection timer countdown scripts

def StartInspect():
    global inspectionVar, inspecting
    timerL["text"] = "15"
    inspectionVar = 15
    timerL.after(1000, RefreshInspect)

def RefreshInspect():
    global inspectionVar, inspecting
    if inspectionVar > 0 and inspecting:
        inspectionVar -= 1
        timerL["text"] = str(inspectionVar)
        timerL.after(1000, RefreshInspect)
    else:
        inspecting = False

# These 2 scripts control the solve timer.
# I've made it to 1/10th of a second, as with 1/100 there's a noticeable delay
# even with 1/10th there is still a delay

def StartSolveTimer():
    global solveTime, timing
    solveL["text"] = "0.00"
    solveTime = 0.00
    solveL.after(100, RefreshTimer)

def RefreshTimer():
    global solveTime, timing
    solveTime += 0.1
    if timing:
        solveL["text"] = str(round(solveTime,2))
        solveL.after(100, RefreshTimer) # this may need to be unindented?
    

def SpacePressed(event):
    global inspecting, timing
    if inspecting: # stop inspecting, start timing
        inspecting = False
        timerL["text"] = ""
        scrambleL.config(fg = "#f0f0f0")
        timing = True
        StartSolveTimer()
    elif timing: # stop timing
        timing = False
        timerL["text"] = "15"
        scrambleL["text"] = GenerateScramble()
        scrambleL.config(fg = "#000000")
        timesT.insert(END, str(round(solveTime,2)) + "\n")
    else: # start inspecting
        inspecting = True
        solveL["text"] = "0.00"
        StartInspect()

def DisplayScramble(event):
    scrambleL.config(fg = "#000000")
    scrambleL["text"] = GenerateScramble()


window.bind("<space>", SpacePressed)

def KeyPressed(event): # function called when key pressed; test, no purpose
    print("KeyPressed running")
    keyL = Label(window, text = "Space pressed!" + event.char)
    keyL.place(x=200,y=200)

window.mainloop()


