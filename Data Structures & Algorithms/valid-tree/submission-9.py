class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: backtracking, bfs, iteration
        """
        adjs = {vertex: set() for vertex in range(n)}
        for u, v in edges:
            if u == v:
                return False
            adjs[u].add(v)
            adjs[v].add(u)

        queue = deque([(0, -1)])
        visited = set()

        def bfs():
            while queue:
                node, parent_node = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)

                for next_node in adjs[node]:
                    if next_node != parent_node:
                        queue.append((next_node, node))
            
            return len(visited) == n

        return bfs()