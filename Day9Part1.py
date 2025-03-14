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


def reArrange(inputList):
    for i in range(len(inputList)-1, 0, -1):
        if inputList[i] != '.':
            temp = inputList[i]
            for j in range(len(inputList)):
                if inputList[j] == '.':
                    inputList[j] = temp
                    inputList[i] = '.'
                    break
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
problemList = reArrange(problemList)
calculate(problemList)