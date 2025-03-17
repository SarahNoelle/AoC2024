from collections import deque

def readFile(filename):
    with open(filename, "r") as f:
        grid = [[int(c) for c in line.strip()] for line in f if line.strip()]
    if not grid:
        raise ValueError("Wrong input.")
    return grid


def findTrails(grid):
    res = 0
    row, col = len(grid), len(grid[0])
    # for each row and column start the search
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                temp = BFS(grid, r, c)
                res += temp
    return res


def BFS(grid, startRow, startCol):

    rows, cols = len(grid), len(grid[0])
    queue = deque([(startRow, startCol)])
    visited = set ()
    visited.add((startRow, startCol))
    found9 = set ()

    while queue:
        r, c = queue.popleft()

        if grid[r][c] == 9:
            found9.add((r, c))
            continue

        #search all 4 direction
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            newRow, newCol = r + i, c + j
            if 0 <= newRow < rows and 0 <= newCol < cols: #index still in the grid range
                if (newRow, newCol) not in visited and grid[newRow][newCol] == grid[r][c] + 1:
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))

    return len(found9)



grid = readFile("input1.txt")
result = findTrails(grid)
print("Result:", result)