class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col, distance):
            grid[row][col] = distance
            visited_area.add((row, col))

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for di, dj in directions:
                i = row + di
                j = col + dj

                if (0 <= i < rows and
                    0 <= j < cols and
                    not grid[i][j] in (0, 1) and
                    grid[i][j] > distance + 1
                    # and not (i, j) in visited_area
                    ):
                    dfs(i, j, distance + 1)

        for row in range(rows):
            for col in range(cols):
                visited_area = set()

                if grid[row][col] == 0:
                    dfs(row, col, 0)

        return None