class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows = len(grid)  # Get the number of rows
        cols = len(grid[0])  # Get the number of columns
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # Possible 4 directions

        def dfs(row, col, distance):
            if (row < 0 or
                row == rows or  # Check if row out of bounds
                col < 0 or
                col == cols or  # Check if column out of bounds
                grid[row][col] == -1 or  # check if water
                (distance and grid[row][col] == 0) or  # check if starting treasure
                    grid[row][col] < distance):  # check if shorter distance is already found
                return

            grid[row][col] = distance  # Mark the current cell with the distance

            for i, j in directions:
                dfs(row + i, col + j, distance + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:  # check if the cell is a treasure
                    dfs(row, col, 0)  # Start DFS with distance 0