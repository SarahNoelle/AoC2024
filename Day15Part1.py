def readInput(filename):
    with open(filename, "r") as f:
        sections = f.read().strip().split("\n\n")

    warehouseMap = sections[0].split("\n")
    moves = "".join(sections[1].split())

    return warehouseMap, moves


def simulateMovement(map, moves):
    warehouse = [list(row) for row in map]

    
    robotX, robotY = None, None
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                robotX, robotY = i, j
                break

    
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    
    for move in moves:
        dx, dy = directions[move]
        newX, newY = robotX + dx, robotY + dy

       
        if warehouse[newX][newY] == "#":
            continue

        
        if warehouse[newX][newY] == ".":
            warehouse[robotX][robotY] = "."
            warehouse[newX][newY] = "@"
            robotX, robotY = newX, newY

        
        elif warehouse[newX][newY] == "O":
            boxX, boxY = newX + dx, newY + dy

            
            while 0 <= boxX < len(warehouse) and 0 <= boxY < len(warehouse[0]) and warehouse[boxX][boxY] == "O":
                boxX += dx
                boxY += dy

            if 0 <= boxX < len(warehouse) and 0 <= boxY < len(warehouse[0]) and warehouse[boxX][boxY] == ".":
                warehouse[boxX][boxY] = "O"
                warehouse[newX][newY] = "@"
                warehouse[robotX][robotY] = "."
                robotX, robotY = newX, newY

   
    sumGPS = sum(100 * i + j for i in range(len(warehouse)) for j in range(len(warehouse[0])) if warehouse[i][j] == "O")
    return sumGPS



map, moves = readInput('input1.txt')
res = simulateMovement(map, moves)
print(res)
