import random


def init_caves():
    for x in range(grid_size):
        grid.append([1])
        for y in range(grid_size):
            grid[x].append(1)


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
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if random.random() > 0.8:
                grid[i][j] = 0


def get_neighbors():
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
            if not grid[i][j] > 0:
                continue

            neighbors = 0
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < grid_size and 0 <= nj < grid_size:
                    if grid[ni][nj] > 0:
                        neighbors += 1

            grid[i][j] = neighbors


def clean_up():
    for i in range(grid_size):
        for j in range(grid_size):
            if not isinstance(grid[i][j], int):
                continue

            if grid[i][j] <= 4:
                grid[i][j] = 0


size = input(
    "grid size [nums > 100 will be hard to see, 64 recommeded], [just press enter for 64] -> "
)
try:
    grid_size = int(size)
except Exception:
    grid_size = 64
openness = input("openness [just press enter for 6] -> ")
try:
    openness = int(openness)
except Exception:
    openness = 6

grid: list[list] = []
init_caves()
remove_random()


for i in range(openness):
    get_neighbors()
    clean_up()
get_neighbors()

print_generated()
