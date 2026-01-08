import random

from inkex.paths import smooth


def init_caves():
    for x in range(grid_size[0]):
        grid.append([0])
        for y in range(grid_size[1]):
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
            if random.random() > 0.7:
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

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if not isinstance(grid[i][j], int):
                continue

            neighbors = 0
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < grid_size[0] and 0 <= nj < grid_size[1]:
                    if isinstance(grid[ni][nj], int):
                        neighbors += 1

            new_grid[i][j] = neighbors

    return new_grid


def clean_up():
    new_grid = grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if not isinstance(grid[i][j], int):
                continue

            if grid[i][j] <= 3:
                new_grid[i][j] = ""

    return new_grid


grid_size = (64, 64)
grid = []

init_caves()
grid = remove_random()
smoothness = input(
    "smoothness [nums > 1000 will be slow, 100 recommended] [just press enter for 100] -> "
)
try:
    smoothness = int(smoothness)
except Exception:
    smoothness = 100

for i in range(smoothness):
    grid = get_neighbors()
    grid = clean_up()
grid = get_neighbors()
print_generated()
