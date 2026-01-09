import random


def init_caves():
    for x in range(grid_size):
        grid.append([0])
        for y in range(grid_size):
            grid[x].append(0)


def print_generated():
    string = ""
    for i in grid:
        for j in i:
            if j == 0 or j == "":
                string += "   "
                continue
            string += f"[{j}]"
        string += "\n"

    print(string)


def remove_random():
    new_grid = grid
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if random.random() > 0.8:
                new_grid[i][j] = ""

    return new_grid


def get_neighbors():
    new_grid = grid

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for i in range(grid_size):
        for j in range(grid_size):
            if not isinstance(grid[i][j], int):
                continue

            neighbors = 0
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < grid_size and 0 <= nj < grid_size:
                    if isinstance(grid[ni][nj], int):
                        neighbors += 1

            new_grid[i][j] = neighbors

    return new_grid


def clean_up():
    new_grid = grid
    for i in range(grid_size):
        for j in range(grid_size):
            if not isinstance(grid[i][j], int):
                continue

            if grid[i][j] <= 4:
                new_grid[i][j] = ""

    return new_grid


size = input(
    "sqrt of grid size [nums > 100 will be hard to see, 64 recommeded], [just press enter for 64] -> "
)
try:
    grid_size = int(size)
except Exception:
    grid_size = 64

grid = []
init_caves()

grid = remove_random()

openness = input("openness [just press enter for 10] -> ")
try:
    openness = int(openness)
except Exception:
    openness = 10

for i in range(openness):
    grid = get_neighbors()
    grid = clean_up()
grid = get_neighbors()
print_generated()
