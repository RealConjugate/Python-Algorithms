def LongestRun(line): # get longest run of a character that occurs
    longest = 1
    index = 1
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            index += 1
        else:
            if index > longest:
                longest = index
            index = 1
    if index > longest:
        longest = index
    return longest


def ChunkLen(List): # set length of "chunk" representing each char
    maxLen = 0
    for line in List:
        if LongestRun(line) > maxLen:
            maxLen = LongestRun(line)
    return len(str(maxLen)) + 1 


def EncodeLine(line, chunkLen):
    encoded = ""
    run = 1
    char = ""
    for i in range(1, len(line)):
        char = line[i]
        if line[i] == line[i-1]:
            run += 1
        else:
            zeros = ""
            for j in range(1, chunkLen-len(str(run))):
                zeros = zeros + "0"
            encoded = encoded + zeros + str(run) + line[i-1]
            run = 1
            
    zeros = ""
    for j in range(1, chunkLen-len(str(run))):
        zeros = zeros + "0"
    encoded = encoded + zeros + str(run) + char
    return encoded
        

def EncodeFile(List):
    chunkLen = ChunkLen(List)
    lineBreak = ""
    for i in range(0,chunkLen):
        lineBreak = lineBreak + "b"
    emptyLine = ""
    for i in range(0,chunkLen):
        emptyLine = emptyLine + "a"
    encoded = str(chunkLen) + "c" # indicate length of chunk at start
    for line in List:
        if line == "":
            encoded = encoded + emptyLine + lineBreak
        else:
            encoded = encoded + EncodeLine(line, chunkLen) + lineBreak
    return encoded


def DecodeFile(string):
    chunkLen = int(string[slice(0,string.index("c"))])
    index = string.index("c") + 1
    line = ""
    lineList = []
    while index <= len(string) - chunkLen:
        Slice = string[slice(index, index + chunkLen)] # whole chunk, not just number
        if Slice[0] == "b": # line break
            lineList.append(line)
            line = ""
        elif Slice[0] == "a": # empty line
            line = ""
        else:
            char = Slice[chunkLen-1]
            num = int(Slice[slice(0,chunkLen-1)]) # gets number of chars
            i = 0
            while i < num:
                line = line + char
                i += 1
        index += chunkLen
    if not line == "":
        lineList.append(line)
    return lineList


def EncodeInterface():
    print("Enter the file path to encode your ASCII text.")
    valid = False
    while not valid:
        filePath = input(">>> ")
        try:
            file = open(filePath, "r")
            fileLines = file.read().splitlines()
            file.close()
            valid = True
            print(EncodeFile(fileLines))
            Menu()
        except:
            print("Invalid file path. Please retry.")


def DecodeInterface():
    print("Enter the run length encoded string to decode.")
    valid = False
    while not valid:
        string = input(">>> ")
        try:
            List = DecodeFile(string)
            for line in List:
                print(line)
            valid = True
            Menu()
        except:
            print("Invalid input. Please retry.")
        
    
def Menu():
    print("\n")
    print("Run Length Encoding")
    print("Press 1 to encode and press 2 to decode.")
    valid = False
    while not valid:
        Input = input(">>> ")
        if Input == "1":
            valid = True
            EncodeInterface()
        elif Input == "2":
            valid = True
            DecodeInterface()
        else:
            print("Invalid input.")
        
            
Menu()
