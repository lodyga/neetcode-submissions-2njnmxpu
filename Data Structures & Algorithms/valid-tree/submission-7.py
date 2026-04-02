class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adjs = {vertex: set() for vertex in range(n)}
        for u, v in edges:
            if u == v:
                return False
            adjs[u].add(v)
            adjs[v].add(u)

        path = set()
        visited = set()

        def dfs(vertex, prev_vertex):
            if vertex in path:
                return False

            path.add(vertex)
            visited.add(vertex)

            for adj_vertex in adjs[vertex]:
                if (
                    adj_vertex != prev_vertex and 
                    not dfs(adj_vertex, vertex)
                ):
                    return False
            
            path.remove(vertex)
            return True
        
        return dfs(0, -1) and len(visited) == n