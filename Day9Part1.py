def readFile(filename: str):

    with open(filename, "r") as f:
        inputList = f.read().strip()


    workingList = []
    fileId = 0
    isFile = True

    for char in inputList:
        length = int(char)
        if isFile:
            workingList.extend([fileId]*length)
            fileId += 1

        else:
            workingList.extend(['.']*length)
        isFile = not isFile
    
    return workingList


#def reArrange(inputList):
#   for i in range(len(inputList)-1, 0, -1):
#       if inputList[i] != '.':
#           temp = inputList[i]
#           for j in range(len(inputList)):
#                if inputList[j] == '.':
#                    inputList[j] = temp
#                    inputList[i]= '.'
#                    break 

#    return inputList


def reArrangePart2(inputList):
    # Find all files and their starting position and save them in files
    files = {}
    i = 0
    while i < len(inputList):
        if inputList[i] != '.':
            fileID = inputList[i]
            start = i
            while i < len(inputList) and inputList[i] == fileID:
                i += 1
            files[fileID] = (start, i - 1)
        else:
            i += 1

    # Debug: Show found files and their positions
    print("Files and positions:")
    for fileID, (start, end) in files.items():
        print(f"File {fileID}: start = {start}, end = {end}")

    # Move files starting with the highest ID
    for fileID in sorted(files.keys(), reverse=True):
        start, end = files[fileID]
        size = end - start + 1

        # Find free space
        free = None
        i = 0
        while i < len(inputList):
            if inputList[i] == '.':
                j = i
                while j < len(inputList) and inputList[j] == '.':
                    j += 1
                if (j - i) >= size:
                    free = i
                    break
            i += 1

        # Debug: Check the free space found
        print(f"File {fileID}: Looking for space of size {size}. Free space starts at {free}")

        # Move if there is enough space
        if free is not None:
            # Fill old space with '.'
            print(f"Moving file {fileID} from {start} to {free}")
            for k in range(start, end + 1):
                inputList[k] = '.'

            # Place file in new space
            for k in range(size):
                inputList[free + k] = fileID

            # Debug: Output after moving
            print(f"After moving file {fileID}: {''.join(map(str, inputList))}")
        else:
            print(f"File {fileID} could not be moved due to insufficient space.")

    return inputList





def calculate(inputList):
    res = 0
    pos = 0
    for i in range(len(inputList)):
        if inputList[i] != '.':
            # Um sicherzustellen, dass fileID als Zahl behandelt wird
            fileID = int(inputList[i])  # Umwandeln in eine Zahl
            res += fileID * pos
            pos += 1

    print(f"Result: {res}")

inputFile = "input1.txt"
problemList = readFile(inputFile)
problemList = reArrangePart2(problemList)
calculate(problemList)