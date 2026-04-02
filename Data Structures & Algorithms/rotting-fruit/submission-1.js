class Solution {
   /**
    * Time complexity: O(n4)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, recursion, matrix, graph
    * @param {number[][]} grid
    * @return {number}
    */
   orangesRotting(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const visitedCells = new Set();
      const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const gridCopy = Array.from({ length: rows }, () => Array(cols).fill(Infinity))

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (grid[row][col] === 0) {
               gridCopy[row][col] = -1
            }
         }
      }

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (grid[row][col] === 2) {
               dfs(row, col, 0)
            }
         }
      }
      
      let distance = -1;
      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            distance = Math.max(distance, gridCopy[row][col])
         }
      }
      // only water cells
      distance = Math.max(distance, 0);
      return distance === Infinity ? -1 : distance

      function dfs(row, col, distance) {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            grid[row][col] === 0 ||
            gridCopy[row][col] <= distance ||
            visitedCells.has(`${row},${col}`)
         ) return

         gridCopy[row][col] = Math.min(gridCopy[row][col], distance);
         visitedCells.add(`${row},${col}`);
         directions.map(([r, c]) => dfs(row + r, col + c, distance + 1));
         visitedCells.delete(`${row},${col}`);
      }
   };
}