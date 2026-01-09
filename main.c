#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void initCaves(int size, int grid[size][size]) {
  for (int y = 0; y < size; y++) {
    for (int x = 0; x < size; x++) {
      grid[y][x] = 1;
    }
  }
}

void printGenerated(int size, int grid[size][size]) {
  for (int y = 0; y < size; y++) {
    for (int x = 0; x < size; x++) {
      if (grid[y][x] <= 0) {
        printf("   ");
        continue;
      }
      printf("[%d]", grid[y][x]);
    }
    printf("\n");
  }
}

void removeRandom(int size, int grid[size][size]) {
  for (int y = 0; y < size; y++) {
    for (int x = 0; x < size; x++) {
      if ((double)rand() / RAND_MAX <= 0.3) {
        grid[y][x] = 0;
      }
    }
  }
}

void getNeighbors(int size, int grid[size][size]) {
  int sides[8][2] = {{1, 1}, {1, 0},  {1, -1}, {0, -1},
                     {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}};

  for (int y = 0; y < size; y++) {
    for (int x = 0; x < size; x++) {
      if (grid[y][x] <= 0) {
        continue;
      }
      int neighbors = 0;
      for (int i = 0; i < 8; i++) {
        int ni = y + sides[i][0];
        int nj = x + sides[i][1];

        if (ni >= 0 && ni < size && nj >= 0 && nj < size) {
          if (grid[ni][nj] > 0) {
            neighbors += 1;
          }
        }
      }
      grid[y][x] = neighbors;
    }
  }
}

void cleanup(int size, int grid[size][size]) {
  for (int y = 0; y < size; y++) {
    for (int x = 0; x < size; x++) {
      if (grid[y][x] <= 4) {
        grid[y][x] = 0;
      }
    }
  }
}

int main() {
  srand(time(NULL));
  int grid[64][64];

  initCaves(64, grid);
  removeRandom(64, grid);

  getNeighbors(64, grid);
  cleanup(64, grid);
  getNeighbors(64, grid);
  cleanup(64, grid);
  getNeighbors(64, grid);
  cleanup(64, grid);

  getNeighbors(64, grid);

  printGenerated(64, grid);

  return 0;
}
