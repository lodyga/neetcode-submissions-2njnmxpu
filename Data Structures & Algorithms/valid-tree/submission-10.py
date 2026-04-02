class DSU:
    def __init__(self, node_count) -> None:
        self.parents = list(range(node_count))
        self.rank = [1] * node_count
        self.size = node_count

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        elif self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
            self.parents[v] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv
            self.parents[u] = pv
        self.size -= 1
        return True

class Solution:
    def validTree(self, node_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        if len(edges) > node_count - 1:
            return False
        
        dsu = DSU(node_count)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return dsu.size == 1