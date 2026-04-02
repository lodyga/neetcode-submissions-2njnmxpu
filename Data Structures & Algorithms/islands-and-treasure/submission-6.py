from collections import deque

# O(n2), O(n2)
# bfs, iteration, deque
class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
    # def wallsAndGates(self, grid: list[list[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                if (0 <= row < rows and
                    0 <= col < cols and
                    grid[row][col] != -1 and
                        (row, col) not in visited):

                    grid[row][col] = distance
                    visited.add((row, col))

                    for i, j in directions:
                        queue.append((row + i, col + j))
                    
            distance += 1