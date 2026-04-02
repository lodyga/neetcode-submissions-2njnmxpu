class Solution:
    def validTree(self, vertex_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: 
            DS: array
            A: Single-source BFS, cycle detection
        """
        # Tree property: E == V - 1
        if len(edges) != vertex_count - 1:
            return False

        adj_vertices = {vertex: set() for vertex in range(vertex_count)}
        for u, v in edges:
            adj_vertices[u].add(v)
            adj_vertices[v].add(u)

        visited = [False] * vertex_count

        def bfs() -> bool:
            queue = deque([(0, -1)])
            while queue:
                vertex, prev = queue.popleft()
                if visited[vertex]:
                    return False
                visited[vertex] = True

                for adj_vertex in adj_vertices[vertex]:
                    if adj_vertex != prev:
                        queue.append((adj_vertex, vertex))

            return True

        # No cycles and connected.
        return bfs() and all(visited)