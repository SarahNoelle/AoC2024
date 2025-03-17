from collections import deque

def readFile(filename):
    with open(filename, "r") as f:
        grid = [[int(c) for c in line.strip()] for line in f if line.strip()]
    if not grid:
        raise ValueError("Wrong input.")
    return grid


def neighbors(r, c, rows, cols):
    
    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc


def score(grid, trailhead):
    rows, cols = len(grid), len(grid[0])
    queue = deque([trailhead])
    
    score = 0

    while queue:
        r, c = queue.pop()
        
        if grid[r][c] == 9:
            score += 1
            continue

        queue.extend(
            (nr, nc)
            for nr, nc in neighbors(r, c, rows, cols)
            if grid[nr][nc] == grid[r][c] + 1
        )

    return score



def rating(grid):
   
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                count += score(grid, (r, c))  # Rating for every trailhead

    return count



grid = readFile("input1.txt")
res2 = rating(grid)


print("Result Part:", res2)
