# This program uses the first-fit decreasing algorithm.

def Pack(List, size): # List already sorted
    allBins = [[]] # list of lists (bins)
    binSizes = [0]
    for num in List:
        added = False
        i = 0
        while not added and i < len(binSizes):
            if binSizes[i] + num <= size:
                allBins[i].append(num)
                binSizes[i] = binSizes[i] + num # if room in current bin
                added = True
            else:
                i += 1
                
        if not added:
            allBins.append([num])
            binSizes.append(num)
            added = True

    # Calculate a lower bound

    total = 0
    for num in List:
        total += num

    if total > size:
        lowerBound = int((total - (total % size))/size)
        print(str(len(binSizes)) + " bins were used.")
        print("A lower bound for an optimal solution is " + str(lowerBound) + " bins.")
    else:
        lowerBound = 1
        print(str(len(binSizes)) + " bin was used.")
        print("A lower bound for an optimal solution is " + str(lowerBound) + " bin.")
        
    i = 0
    while i < len(allBins):
        print("Bin " + str(i+1) + ": " + str(allBins[i]))
        i += 1

    EnterValidate()

    
def SortDescending(List): # bubble sort
    swaps = 1 # nonzero value

    if len(List) >= 2:
        while swaps != 0:
                swaps = 0
                for i in range(0, len(List)-1):
                    if List[i] < List[i+1]:
                        spare = List[i+1]
                        List[i+1] = List[i]
                        List[i] = spare
                        swaps = swaps + 1
    return List


def EnterValidate():
    print("\n")
    print("Enter the numbers to be packed into bins.")
    print("Example format: 8 10 4 2 8 4 5")
    numbers = input(">>>")

    sliced = Slice(numbers, " ")
    valid = True
    i = 0
    while valid and i < len(sliced):
        if sliced[i].isnumeric():
            sliced[i] = int(sliced[i])
            i += 1
        else:
            valid = False

    if valid:
        print("Enter bin size.")
        binSize = input(">>>")
        if binSize.isnumeric():
            sortedSliced = SortDescending(sliced)
            largestItem = sortedSliced[0]
            if largestItem <= int(binSize):
                Pack(sortedSliced, int(binSize))
            else:
                print("Invalid: bin size is less than largest number.")
                EnterValidate()
        else:
            print("Invalid: bin size must be numeric.")
            EnterValidate()
    else:
        print("Invalid: entries must be numeric. No spaces at the end.")
        EnterValidate()  
    
    
def Slice(string, char):
    string = string + " "
    newList = []
    hold = ""
    for item in string:
        if item == char:
            newList.append(hold)
            hold = ""
        else:
            hold = hold + item
            
    return newList
            
            
EnterValidate()
