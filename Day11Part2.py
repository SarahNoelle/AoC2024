from collections import Counter

def readFile(filename: str):
    with open(filename, "r") as f:
        return Counter(map(int, f.read().strip().split()))  

def applyRules(filename):
    workingList = readFile(filename)

    for _ in range(75):  
        newList = Counter() 

        for stone, count in workingList.items():
            if stone == 0:
                newList[1] += count  

            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                half_len = len(stone_str) // 2
                half1 = int(stone_str[:half_len])
                half2 = int(stone_str[half_len:])
                newList[half1] += count  
                newList[half2] += count

            else:
                newList[stone * 2024] += count  

        workingList = newList  

    print("Res:", sum(workingList.values()))

filename = "Input1.txt"
applyRules(filename)
