class Solution:
    def validTree(self, vertex_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: Single-source DFS, cycle detection
        """
        def dfs(vertex: int) -> bool:
            if visited[vertex]:
                return False

            visited[vertex] = True

            for next_vertex in adjs[vertex]:
                adjs[next_vertex].remove(vertex)

                if dfs(next_vertex) is False:
                    return False

            return True

        # Tree property: E == V - 1
        if len(edges) != vertex_count - 1:
            return False

        if vertex_count == 1:
            return len(edges) == 0

        adjs = {}
        visited = [False] * vertex_count

        for u, v in edges:
            if u == v:
                return False

            if u not in adjs:
                adjs[u] = set()

            if v not in adjs:
                adjs[v] = set()

            adjs[u].add(v)
            adjs[v].add(u)

        res = dfs(edges[0][0])

        # No cycles and connected.
        return res and all(visited)

