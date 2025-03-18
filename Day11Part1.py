def readFile(filename: str):
    with open(filename, "r") as f:
        return list(map(int, f.read().strip().split()))  # List of numbers


def applyRules(filename):
    workingList = readFile(filename)
    
    for x in range(25):  # 25 iterations as demanded
        newList = []  

        for stone in workingList:
            if stone == 0:
                newList.append(1)  # Rule 1

            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                half_len = len(stone_str) // 2
                half1 = int(stone_str[:half_len]) #slicing to divide the stone 
                half2 = int(stone_str[half_len:])
                newList.extend([half1, half2])  # Rule 2

            else:
                newList.append(stone * 2024)  # Rule 3

        workingList = newList  

    print("Res:", len(workingList))


filename = "Input1.txt"
applyRules(filename)
