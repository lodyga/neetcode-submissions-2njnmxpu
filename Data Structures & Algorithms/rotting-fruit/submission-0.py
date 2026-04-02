class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Time complexity: O(n4)
        Auxiliary space complexity: O(n2)
        Tags: dfs, recursion, matrix, graph
        """
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = [[float("inf")] * cols for _ in range(rows)]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()

        def dfs(row, col, distance):
            if (row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                grid[row][col] == 0 or
                grid_copy[row][col] <= distance or
                    (row, col) in visited_cells):
                return

            grid_copy[row][col] = min(grid_copy[row][col], distance)
            visited_cells.add((row, col))

            for r, c in directions:
                dfs(row + r, col + c, distance + 1)

            visited_cells.remove((row, col))

        # replace water 0 wtith -1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    grid_copy[row][col] = -1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    dfs(row, col, 0)

        if any(float("inf") in row for row in grid_copy):
            return -1
        else:
            ans = max(max(row) for row in grid_copy)
            return 0 if ans == - 1 else ans