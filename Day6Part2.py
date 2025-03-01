
def readFile(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    if not grid:
        raise ValueError("Wrong input.")
    return grid



def simulateMovement(grid):
    rows = len(grid)
    columns = len(grid[0])

    
    pos, dir = findGuard(grid)
    
    if pos is None:
        raise ValueError("No guard found.")

    
    trace = {}

    while True:
        
        if pos in trace and dir in trace[pos]:
            return trace  
        
        
        if pos not in trace:
            trace[pos] = []
        trace[pos].append(dir)

        
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])

        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < columns):
            return -1  

        
        if grid[next_pos[0]][next_pos[1]] == '#':
            dir = turnRight(dir)
        else:
            pos = next_pos



def findGuard(grid):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                return (r, c), directions[cell]
    return None, None  



def turnRight(dir):
    turns = {
        (-1, 0): (0, 1),  # up, right 
        (0, 1): (1, 0),   # right, down  
        (1, 0): (0, -1),  # down, left 
        (0, -1): (-1, 0)  # left, up 
    }
    return turns[dir]



def findLoop(grid):
    loop_positions = set()
    rows, columns = len(grid), len(grid[0])

    
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == '.':
                grid[r][c] = '#' 
                
                if simulateMovement(grid) != -1:
                    loop_positions.add((r, c))  
                grid[r][c] = '.'  

    return loop_positions


filename = "input1.txt"
mapGrid = readFile(filename)
loop_positions = findLoop(mapGrid)

print("Number of loop positions:", len(loop_positions))
