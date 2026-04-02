class Solution:
    def countComponents(self, node_count: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        BFS
        """
        adjs = {node: set() for node in range(node_count)}
        for u, v in edges:
            if u != v:
                adjs[u].add(v)
                adjs[v].add(u)
        
        visited = [False] * node_count
        component_count = 0

        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                visited[node] = True

                for adj_node in adjs[node]:
                    if not visited[adj_node]:
                        queue.append(adj_node)

        for node in range(node_count):
            if not visited[node]:
                bfs(node)
                component_count += 1
        
        return component_count