# This is a basic tkinter tutorial program, to help people create simple GUIs.

from tkinter import * # import tkinter module

# create window and set title (and fixed size if needed)

window = Tk()
window.title("Tkinter Tutorial")
window.geometry("420x250")

# ---- Create Frames ----

BigFrame = Frame(window) # everything goes in this
BigFrame.grid() # puts in grid

# create 4 large frames contained in BigFrame - put in grid

LabelFrame = Frame(BigFrame)
LabelFrame.grid(row=0,column=0)
ButtonFrame = Frame(BigFrame)
ButtonFrame.grid(row=0,column=1)
EntryFrame = Frame(BigFrame)
EntryFrame.grid(row=1,column=0)
TextFrame = Frame(BigFrame)
TextFrame.grid(row=1,column=1)

# ---- Label Frame ----

# add labels to LabelFrame, containing text - specify (master frame, text, width)
# all need to be put in the grid as shown - can also create frames for each label
# to position more precisely

label1 = Label(LabelFrame, text = "Welcome to this tkinter tutorial!", width = 30)
label1.grid(row=0,column=0)
label2 = Label(LabelFrame, text = "These are labels, containing text.", width = 30)
label2.grid(row=1,column=0)
label3 = Label(LabelFrame, text = "Here we have buttons, entries and text.", width = 30)
label3.grid(row=2,column=0)
label4 = Label(LabelFrame, text = "This shows how everything works.", width = 30)
label4.grid(row=3,column=0)


# ---- Button Frame ----

# Create 2 frames: one for number incrementing buttons and one for text

NumberFrame = Frame(ButtonFrame)
NumberFrame.grid(row=0,column=0)
ColourChangeFrame = Frame(ButtonFrame)
ColourChangeFrame.grid(row=1,column=0)

def minus(): # note syntax to get text from a label
    currentInt = int(integer["text"])
    integer["text"] = str(currentInt - 1)

def plus():
    currentInt = int(integer["text"])
    integer["text"] = str(currentInt + 1)
    

labelgap = Label(NumberFrame, text = "", width = 5) # labels can also create spaces
labelgap.grid(row=0,column=0)

# create buttons to subtract/add 1

minus = Button(
    master = NumberFrame,
    text = "-",
    command = minus,
    bg = "#f09481",
    fg = "black",
    width = 4
    )
minus.grid(row=0,column=1)

plus = Button(
    master = NumberFrame,
    text = "+",
    command = plus,
    bg = "#d1ffcc",
    fg = "black",
    width = 4
    )
plus.grid(row=0,column=2)
    
# create label for integer

integer = Label(NumberFrame, text = "0", width = 10)
integer.grid(row=0,column=3)

# another space

hlabelgap = Label(NumberFrame, text = "", width = 5)
hlabelgap.grid(row=1,column=0)

# dropdown menu to select colour - specify variable first with StringVar, then options

colourVar = StringVar()
colourVar.set("Select colour")
dropdown = OptionMenu(ColourChangeFrame, colourVar, "Green", "Blue", "Red", "Yellow")
dropdown.grid(row=0,column=0)

def SetColour():
    colour = colourVar.get().lower() # syntax to get variable from dropdown
    colourText.config(fg = colour) # change colour of label text

# button to change the colour, once one is selected
    
colourGo = Button(
    master = ColourChangeFrame,
    text = "Go",
    command = SetColour,
    bg = "#d1ffcc",
    fg = "black",
    width = 4
    )
colourGo.grid(row=0,column=1)

colourText = Label(ColourChangeFrame, text = "   text", width = 6)
colourText.grid(row=0,column=2)

# ---- Entry Frame ----

# another gap

hlabelgap2 = Label(EntryFrame, text = "", width = 5)
hlabelgap2.grid(row=0,column=0)

entrylabel = Label(EntryFrame, text = "You can enter text in this field.", width = 25)
entrylabel.grid(row=1,column=0)

# create an "entry" - single line text field

field = Entry(master = EntryFrame, width = 17)
field.grid(row=2,column=0)

def MakeUpper():
    text = field.get() # get text from entry, and make uppercase
    upperlabel["text"] = text.upper()

# again a button to execute
    
Upper = Button(
    master = EntryFrame,
    text = "Upper",
    command = MakeUpper,
    bg = "#d1ffcc",
    fg = "black",
    width = 4
    )
Upper.grid(row=2,column=1)

# this label stores uppercase text once typed

upperlabel = Label(EntryFrame, text = "", width = 20)
upperlabel.grid(row=3,column=0)


# ---- Text Frame ----

boxlabel = Label(TextFrame, text = "You can enter text here.")
boxlabel.grid(row=0,column=0)

# creates a text box (multi-line)

textbox = Text(TextFrame, height = 5, width = 20)
textbox.grid(row=1,column=0)


# must include window.mainloop() for tkinter window to run
window.mainloop()
