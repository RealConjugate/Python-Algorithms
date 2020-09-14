from math import gcd
from decimal import Decimal
from tkinter import *

window = Tk()
window.title("Simplex Algorithm 2Var")


def InitialTable(a,b,c,d,e,f,g,h):
    array = []
    array.append([c,d,(1,1),(0,1)])
    array.append([f,g,(0,1),(1,1)])
    array.append([(-1*a[0],a[1]),(-1*b[0],b[1]),(0,1),(0,1)])
    values = [e,h,(0,1)]
    basicVars = ["r","s","P"]
    
    return (array, basicVars)


def Iterate(array, basicVars, values): # Maximising P: x,y,r,s>=0. Lists contain tuples
    columns = ["x","y","r","s"]
    negative = []
    numList = []
    for num in array[2]: # array[2] is objective variable row
        if Sign(num) == "negative":
            negative.append(float(num[0]/num[1])) # float to compare values
            numList.append(num)
    if not negative == []:
        mostNegativeFloat = min(negative)
        mostNegative = numList[negative.index(mostNegativeFloat)]
        pivotCol = array[2].index(mostNegative)

        theta = [Div(values[0],array[0][pivotCol]), Div(values[1],array[1][pivotCol])]
        smallestPositive = (0,1) # zero tuple
        for value in theta:
            if Sign(value) == "positive":
                if Sign(smallestPositive) == "zero" or Sign(Subt(value, smallestPositive)) == "negative":
                    smallestPositive = value
                
        if not Sign(smallestPositive) == "zero":
            pivotRow = theta.index(smallestPositive)
            pivot = array[pivotRow][pivotCol]

            newArray = [[],[],[]]
            newValues = []
            dividedRow = []
            for item in array[pivotRow]:
                dividedRow.append(Div(item,pivot))
            for i in range(0,3):
                if i == pivotRow:
                    newArray[i] = dividedRow
                    newValues.append(Div(values[i],pivot))
                else:
                    for j in range(0,4):
                        newArray[i].append(Subt(array[i][j],Mult(array[i][pivotCol],dividedRow[j])))
                    newValues.append(Subt(values[i],Mult(array[i][pivotCol],Div(values[pivotRow],pivot))))

            newBasicVars = []
            for var in basicVars:
                if var == basicVars[pivotRow]:
                    newBasicVars.append(columns[pivotCol])
                else:
                    newBasicVars.append(var)

            Iterate(newArray,newBasicVars,newValues)
            

    else:
        print("Optimal solution found")
        pLabel["text"] = basicVars[2] + " = " + GetString(values[2])
        
        var1["text"] = basicVars[0] + " = " + GetString(values[0])
        var2["text"] = basicVars[1] + " = " + GetString(values[1])

        if "x" in basicVars:
            var1["text"] = "x = " + GetString(values[basicVars.index("x")])
        else:
            var1["text"] = "x = 0"
        if "y" in basicVars:
            var2["text"] = "y = " + GetString(values[basicVars.index("y")])
        else:
            var2["text"] = "y = 0"
                


def StringToRatio(string): # string into reduced fraction as tuple
    if "/" in string: # string already "floatable" - only one /
        index = string.index("/")
        numerator = int(string[0:index])
        denominator = int(string[index + 1:len(string)])
        return (numerator, denominator)
    else:
        return Decimal(string).as_integer_ratio()


def IsStrFloatable(string): # checks if string can be written as fraction
    if "/" in string:
        index = string.index("/") # first instance
        numerator = string[0:index]
        denominator = string[index + 1:len(string)]
        # If >1 / in string we get ValueError        
        try:
            int(numerator)
            try:
                int(denominator)
                return True
            except ValueError:
                return False            
        except ValueError:
            return False
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def Simplify(pair): # simplifies tuple
    numerator = pair[0]
    denominator = pair[1]
    if denominator < 0:
        numerator = -1 * numerator
        denominator = -1 * denominator
    GCD = gcd(numerator, denominator)
    numerator = int(numerator / GCD)
    denominator = int(denominator / GCD)
    return (numerator, denominator)

def Div(V,W):
    return Simplify((V[0]*W[1], V[1]*W[0]))

def Mult(V,W):
    return Simplify((V[0]*W[0],V[1]*W[1]))

def Subt(V,W):
    numerator = V[0]*W[1] - W[0]*V[1]
    denominator = V[1]*W[1]
    return Simplify((numerator, denominator))

def Sign(fraction):
    fraction = Simplify(fraction)
    if fraction[0] == 0:
        return "zero"
    if fraction[0] > 0:
        return "positive"
    if fraction[0] < 0:
        return "negative"
    
def GetString(pair): # tuple --> fraction string
    numerator = pair[0]
    denominator = pair[1]
    if denominator == 1:
        return str(numerator)
    else:
        return str(numerator) + "/" + str(denominator)

def Validate():
    a = EntryPX.get()
    b = EntryPY.get()
    c = entryx1.get()
    d = entryy1.get()
    e = entryval1.get()
    f = entryx2.get()
    g = entryy2.get()
    h = entryval2.get()
    strings = [a,b,c,d,e,f,g,h]
    valid = True
    for item in strings:
        if not IsStrFloatable(item):
            valid = False

    if valid:
        a = StringToRatio(a)
        b = StringToRatio(b)
        c = StringToRatio(c)
        d = StringToRatio(d)
        e = StringToRatio(e)
        f = StringToRatio(f)
        g = StringToRatio(g)
        h = StringToRatio(h)

        strings = [a,b,c,d,e,f,g,h]
        
        if valid:
            print(strings)
            Iterate(InitialTable(a,b,c,d,e,f,g,h)[0],InitialTable(a,b,c,d,e,f,g,h)[1],[e,h,(0,1)])
    
# GUI Creation

Fconstraints1 = Frame(window)
constraints1 = Label(Fconstraints1, text = "Enter positive entries.")
constraints1.grid(row=0,column=0)
Fconstraints2 = Frame(window)
constraints2 = Label(Fconstraints2, text = "Input as int/fraction/decimal.")
constraints2.grid(row=0,column=0)
inputFrame = Frame(window)
FMaximise = Frame(inputFrame)
maximise = Label(FMaximise, text = "Maximise", width = 20)
maximise.grid(row=0,column=0)
FMaximise.grid(row=0,column=0)
FGiven = Frame(inputFrame)
given = Label(FGiven, text = "given", width = 20)
given.grid(row=0,column=0)
FGiven.grid(row=1,column=0)
gap1 = Frame(window)
space = Label(gap1, text = " ")
space.grid(row=0,column=0)
gap1.grid(row=2,column=0)
PRow = Frame(inputFrame)
labelP = Label(PRow, text = "P =")
labelP.grid(row=0,column=0)
EntryPX = Entry(PRow, width = 4)
EntryPX.grid(row=0,column=1)
labelPX = Label(PRow, text = "x +")
labelPX.grid(row=0,column=2)
EntryPY = Entry(PRow, width = 4)
EntryPY.grid(row=0,column=3)
labelPY = Label(PRow, text = "y")
labelPY.grid(row=0,column=4)
PRow.grid(row=0,column=1)
Row1 = Frame(inputFrame)
entryx1 = Entry(Row1, width = 4)
entryx1.grid(row=0,column=0)
labelx1 = Label(Row1, text = "x +")
labelx1.grid(row=0,column=1)
entryy1 = Entry(Row1, width = 4)
entryy1.grid(row=0,column=2)
labely1 = Label(Row1, text = "y <=")
labely1.grid(row=0,column=3)
entryval1 = Entry(Row1, width = 4)
entryval1.grid(row=0,column=4)
Row1.grid(row=1,column=1)
Row2 = Frame(inputFrame)
entryx2 = Entry(Row2, width = 4)
entryx2.grid(row=0,column=0)
labelx2 = Label(Row2, text = "x +")
labelx2.grid(row=0,column=1)
entryy2 = Entry(Row2, width = 4)
entryy2.grid(row=0,column=2)
labely2 = Label(Row2, text = "y <=")
labely2.grid(row=0,column=3)
entryval2 = Entry(Row2, width = 4)
entryval2.grid(row=0,column=4)
Row2.grid(row=2,column=1)
nonnegative = Frame(inputFrame)
label = Label(nonnegative, text = "x, y >= 0")
label.grid(row=0,column=0)
nonnegative.grid(row=3,column=1)
frameButton = Frame(inputFrame)
button = Button(
    master = frameButton,
    text = "Execute",
    command = Validate,
    bg = "#1E7800",
    fg = "#FFFFFF"
    )
button.grid(row=0,column=0)
frameButton.grid(row=4, column=1)
pFrame = Frame(inputFrame)
pLabel = Label(pFrame, text = "")
pLabel.grid(row=0,column=0)
pFrame.grid(row=5, column=1)
var1Frame = Frame(inputFrame)
var1 = Label(var1Frame, text = "")
var1.grid(row=0,column=0)
var2Frame = Frame(inputFrame)
var2 = Label(var2Frame, text = "")
var2.grid(row=0,column=0)
var1Frame.grid(row=5, column=0)
var2Frame.grid(row=6, column=0)
Fconstraints1.grid(row=0,column=0)
Fconstraints2.grid(row=1,column=0)
inputFrame.grid(row=3,column=0)

window.mainloop()
