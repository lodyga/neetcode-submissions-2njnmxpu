class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        counter = 0
        visited_nodes = set()

        adjacencies = {index: [] for index in range(n)}
        for node1, node2 in edges:
            adjacencies[node1].append(node2)
            adjacencies[node2].append(node1)

        def dfs(node):
            if node in visited_nodes:
                return

            visited_nodes.add(node)

            for adjacent_node in adjacencies[node]:
                dfs(adjacent_node)

        for node in adjacencies:
            if node not in visited_nodes:
                counter += 1
                dfs(node)

        return counter