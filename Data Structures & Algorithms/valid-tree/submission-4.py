class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: backtracking, dfs, recursion
        """
        if edges == [] or edges == [[]]:
            return True
        
        visited = set()
        tree = {}

        for parent, child in edges:
            if parent not in tree:
                tree[parent] = set()
            tree[parent].add(child)

            if child not in tree:
                tree[child] = set()
            tree[child].add(parent)

        def dfs(parent, prev_node):
            # visit every node only once
            if parent in visited:
                return False
            visited.add(parent)
            
            for child in tree[parent]:
                # exclude child -> parend backtracking
                if child == prev_node:
                    continue
                elif not dfs(child, parent):
                    return False        
            
            return True 

        # no cycles and connected
        return dfs(0, -1) and len(visited) == n