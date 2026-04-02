class Solution {
  /**
   * @param {number[][]} grid
   */
  islandsAndTreasure(grid) {
    const rows = grid.length;
    const cols = grid[0].length;

    const dfs = (row, col, distance) => {
      grid[row][col] = distance;
      const directions = [[0, 1], [1, 0], [-1, 0], [0, -1]];

      for (const [di, dj] of directions) {
        const i = row + di;
        const j = col + dj;

        if (
          i < rows &&
          j < cols &&
          i >= 0 &&
          j >= 0 &&
          grid[i][j] != 0 &&
          grid[i][j] != -1 &&
          grid[i][j] > distance + 1
        ) {
          dfs(i, j, distance + 1)
        }
      }
    }

    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < cols; col++) {
        if (grid[row][col] === 0) {
          dfs(row, col, 0)
        }
      }
    }
    return null
  }
}