class Solution {
  /**
   * @param {number[][]} grid
   */
  islandsAndTreasure(grid) {
    const rows = grid.length;  // Get the number of rows
    const cols = grid[0].length;  // Get the number of columns
    const queue = [];  // Initialize an empty queue for BFS
    const visitedLand = new Set();  // Set to keep track of visited cells

    const bfs = (row, col) => {
      const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];  // Define 4 possible directions (right, down, left, up)

      for (const [di, dj] of directions) {  // Iterate over each direction
        const i = row + di;  // Calculate new row
        const j = col + dj;  // Calculate new column

        if (
          i < rows &&  // Ensure row is within bounds
          j < cols &&  // Ensure column is within bounds
          i >= 0 &&  // Ensure row is not negative
          j >= 0 &&  // Ensure column is not negative
          grid[i][j] != -1 &&  // Skip if the cell is water or already processed (-1)
          !visitedLand.has(`${i},${j}`)  // Skip if the cell has already been visited
        ) {
          queue.push([i, j]);  // Add valid neighboring cells to the queue
          visitedLand.add(`${i},${j}`);  // Mark as visited immediately when enqueued
        }
      }
    };

    for (let row = 0; row < rows; row++) {  // Iterate through each row
      for (let col = 0; col < cols; col++) {  // Iterate through each column
        if (grid[row][col] === 0) {  // If the cell is land (0)
          queue.push([row, col]);  // Add the land cell to the queue
          visitedLand.add(`${row},${col}`);  // Mark it as visited when added to the queue
        }
      }
    }

    let distance = 0;  // Initialize distance from the treasure

    while (queue.length !== 0) {  // Continue while there are cells in the queue
      let queueLength = queue.length;  // Get the number of cells in the current layer

      for (let index = 0; index < queueLength; index++) {  // Iterate over all cells in the current queue
        const [row, col] = queue.shift();  // Dequeue the next cell
        grid[row][col] = distance;  // Set the distance in the grid
        bfs(row, col);  // Explore the neighboring cells
      }
      distance++;  // Increment the distance for the next layer of cells
    }

    return null;  // Return the modified grid
  }
}