class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        """
        parent = list(range(n))
        rank = [1] * n

        # find root parent
        def find(node):
            # node = root  # delete?

            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        # union nodes
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return 0
            elif rank[root2] > rank[root1]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]
            return 1

        counter = n
        for node1, node2 in edges:
            counter -= union(node1, node2)
        
        return counter