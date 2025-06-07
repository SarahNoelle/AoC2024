def readFile(filename):
    #test
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    if not grid:
        raise ValueError("Wrong Input.")
    return grid


def simulateMovement(grid):
    
    rows = len(grid)
    columns = len(grid[0])

    pos, dir = findGuard(grid)
    if pos is None:
        raise ValueError("Guard not found.")

    seen = set()

    while True:
        seen.add(pos)
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])

        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < columns):
            break #Guard leaves Map

        # Guard turns
        if grid[next_pos[0]][next_pos[1]] == '#':
            dir = turnRight(dir)
        else:
            pos = next_pos

    print("Visited Positions", len(seen))
    return len(seen)


def findGuard(grid):
    
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                return (r, c), directions[cell]
    return None, None  # Guard not found


def turnRight(dir):
    
    turns = {
        (-1, 0): (0, 1),  # up, right 
        (0, 1): (1, 0),   # right down
        (1, 0): (0, -1),  # down, left
        (0, -1): (-1, 0)  # ←left, up
    }
    return turns[dir]



filename = "input1.txt"
mapGrid = readFile(filename)
simulateMovement(mapGrid)
