import tkinter as tk
import random

# Create window and frames

window = tk.Tk()
window.title("Strong Password Generator")

frameHeading = tk.Frame(master = window)
heading = tk.Label(master = frameHeading, text = "Generates a strong password.")
heading.grid(row=0, column=0)

frameDescription = tk.Frame(master = window)
description = tk.Label(master = frameDescription, text = "Contains at least one uppercase, lowercase, digit and symbol character.")
description.grid(row=0, column=0)

entryGrid = tk.Frame(master = window)

frameMin = tk.Frame(master = entryGrid)
frameMax = tk.Frame(master = entryGrid)
frameMinLabel = tk.Frame(master = entryGrid)
frameMaxLabel = tk.Frame(master = entryGrid)

enterMin = tk.Entry(master = frameMin, width = 7)
enterMax = tk.Entry(master = frameMax, width = 7)
labelMin = tk.Label(master = frameMinLabel, text = "Min. chars (at least 8)")
labelMax = tk.Label(master = frameMaxLabel, text = "Max. chars (at most 25)")

enterMin.grid(row=0, column=0)
enterMax.grid(row=0, column=0)
labelMin.grid(row=0, column=0)
labelMax.grid(row=0, column=0)

frameMin.grid(row=0, column=0)
frameMax.grid(row=0, column=1)
frameMinLabel.grid(row=1, column=0)
frameMaxLabel.grid(row=1, column=1)


# Functions

def validate():
    lowerBound = enterMin.get()
    upperBound = enterMax.get() # strings

    if lowerBound.isnumeric() and upperBound.isnumeric():
        lowerBound = int(lowerBound)
        upperBound = int(upperBound)
        if lowerBound >= 8 and upperBound <= 25 and lowerBound <= upperBound:
            length = random.randint(lowerBound, upperBound)
            display["text"] = generate(length)
    


def generate(length):
    import string
    typeList = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    allChars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    i = 0
    indices = [] # generates [0,1,...,length-1]
    while i < length:
        indices.append(i)
        i += 1

    # Generate indices for lowercase, uppercase, digit and punctuation (specialIndices) in that order

    specialIndices = []
    
    for i in range(0,4):
        index = random.randint(0, len(indices)-1) # random position for each character type
        specialIndices.append(indices[index])
        indices.remove(indices[index]) # Each number is only in indices once - remove is fine

    password = ""
    
    for i in range(0, length):
        if i in specialIndices:
            position = specialIndices.index(i) # only appears once
            string = typeList[position]
            password = password + string[random.randint(0, len(string)-1)]
        else:
            password = password + allChars[random.randint(0, len(allChars)-1)]
            
    return(password)


# Remaining frames

frameButton = tk.Frame(master = window)
button = tk.Button(master = frameButton, text = "Generate Password", command = validate, fg = "#FFFFFF", bg = "#1E7800")
button.grid(row=0, column=0)

frameDisplay = tk.Frame(master = window)
display = tk.Label(master = frameDisplay)
display.grid(row=0, column=0)


# Put frames in grid

frameHeading.grid(row=0, column=0)
frameDescription.grid(row=1, column=0)
entryGrid.grid(row=2, column=0)
frameButton.grid(row=3, column=0)
frameDisplay.grid(row=4, column=0)

window.mainloop()
