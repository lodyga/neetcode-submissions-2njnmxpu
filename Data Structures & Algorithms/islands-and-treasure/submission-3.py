from collections import deque  # Import deque for efficient queue operations

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows = len(grid)  # Get the number of rows
        cols = len(grid[0])  # Get the number of columns
        queue = deque()  # Initialize a queue for BFS
        visited_land = set()  # Set to keep track of visited land

        def bfs(row, col):
            # Check if the cell is out of bounds, water (-1), or already visited
            if (not 0 <= row < rows or
                not 0 <= col < cols or
                grid[row][col] == -1 or
                (row, col) in visited_land
            ):
                return  # Stop if any condition is met
            
            queue.append((row, col))  # Add the cell to the queue
            visited_land.add((row, col))  # Mark the cell as visited

        for row in range(rows):  # Iterate over each row
            for col in range(cols):  # Iterate over each column
                if grid[row][col] == 0:  # If the cell is land (0)
                    queue.append((row, col))  # Add the land cell to the queue
                    visited_land.add((row, col))  # Mark it as visited

        distance = 0  # Initialize distance from the treasure

        while queue:  # While there are cells to process
            for _ in range(len(queue)):  # Process each cell in the current layer
                row, col = queue.popleft()  # Get the next cell from the queue
                grid[row][col] = distance  # Set the current distance in the grid
                bfs(row + 1, col)  # Explore the cell below
                bfs(row, col + 1)  # Explore the cell to the right
                bfs(row - 1, col)  # Explore the cell above
                bfs(row, col - 1)  # Explore the cell to the left

            distance += 1  # Increment distance for the next layer

        return None  # Return the modified grid