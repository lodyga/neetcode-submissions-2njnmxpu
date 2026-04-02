class Solution:
    def validTree(self, node_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: 
            DS: array
            A: Single-source DFS, cycle detection
        """
        # Tree property: E == V - 1
        if len(edges) != node_count - 1:
            return False

        adj_nodes = {node: set() for node in range(node_count)}
        for u, v in edges:
            adj_nodes[u].add(v)
            adj_nodes[v].add(u)

        visited = [False] * node_count

        def dfs(node: int, prev: int) -> bool:
            if visited[node]:
                return False

            visited[node] = True

            for adj_node in adj_nodes[node]:
                if (
                    adj_node != prev and 
                    dfs(adj_node, node) is False
                ):
                    return False

            return True

        # No cycles and connected.
        return dfs(0, -1) and all(visited)