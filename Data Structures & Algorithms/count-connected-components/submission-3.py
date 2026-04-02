class Solution:
    def countComponents(self, node_count: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DFS
        """
        adjs = {node: set() for node in range(node_count)}
        for u, v in edges:
            if u != v:
                adjs[u].add(v)
                adjs[v].add(u)
        
        visited = [False] * node_count
        component_count = 0

        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = True

            for adj_node in adjs[node]:
                dfs(adj_node)

        for node in range(node_count):
            if not visited[node]:
                dfs(node)
                component_count += 1
        
        return component_count