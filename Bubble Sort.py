# Bubble Sort


def Menu():
    print("")
    print("Enter 1 to sort a list. Enter 2 to exit the program.")
    selection = input(">>> ")

    if selection == "1":
        UserEnter()
    elif selection == "2":
        exit
    else:
        print("Invalid input. Please try again.")
        Menu()


# User enters list

def UserEnter():
    print("")
    print("Please enter your unsorted list of numbers. Example: 3 56 1.2 -4 20 ")
    unsortedVar = input(">>> ")

    validOrder = False

    while validOrder == False:
        print("Enter 1 to sort into ascending order. Enter 2 to sort into descending order.")
        orderInput = input(">>> ")
        if orderInput == "1":
            order = "a"
            validOrder = True
        elif orderInput == "2":
            order = "d"
            validOrder = True
        else:
            print("Invalid input. Please try again.")
            print("")

    Slice(unsortedVar + " ", order)


# Slices the unsorted string variable into numbers

def Slice(string, order):
    holder = "" # holds each number before placing in list
    unsortedList = []

    charLength = len(string)
    i = 0

    for i in range(0, charLength):
        if string[i] == " ":
            if holder == "":
                i = i + 1
            else:
                unsortedList.append(holder)
                holder = ""
                i = i + 1
        else:
            holder = holder + string[i]
            i = i + 1

    CheckInput(unsortedList, order)



# Checks that all entries are real numbers

def CheckInput(List, order):
    i = 0
    invalidFound = False
    floatList = []

    while i >= 0 and i < len(List) and invalidFound == False:
        try:
            floatList.append(float(List[i]))
            i = i + 1
        except:
            i = i + 1
            invalidFound = True
            
    if invalidFound == False:
        Sort(floatList, order)
    else:
        print("Your input is invalid. All entries in the list must be real decimal numbers.")
        UserEnter()


#Sorts the list

def Sort(List, order):
    swaps = 1 # nonzero value

    if order == "a": # ascending
        while swaps != 0: # loop checks "swaps" value before executing
            swaps = 0
            for i in range(0, len(List)-1):
                if List[i] > List[i+1]:
                    spare = List[i+1]
                    List[i+1] = List[i]
                    List[i] = spare
                    swaps = swaps + 1
                    
    elif order == "d": # descending
        while swaps != 0:
            swaps = 0
            for i in range(0, len(List)-1):
                if List[i] < List[i+1]:
                    spare = List[i+1]
                    List[i+1] = List[i]
                    List[i] = spare
                    swaps = swaps + 1
        
    Int(List)


# Replaces integer valued floats with integers (e.g. 12.0 -> 12)
# Displays sorted list

def Int(List):
    sortedList = []
    
    for item in List:
        length = len(str(item))
        if str(item)[length-2] + str(item)[length-1] == ".0":
            sortedList.append(int(item))
        else:
            sortedList.append(item)

    sortedVar = ""
    for item in sortedList:
        sortedVar = sortedVar + str(item) + " "

    print("")
    print(sortedVar)
    print("")
    Menu()
        

# Initialisation

print("----Bubble Sort----")
print("This program uses the bubble sort algorithm to sort numbers.") 
Menu()

