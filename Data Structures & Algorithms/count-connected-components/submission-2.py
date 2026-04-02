class DSU:
    def __init__(self, node_count) -> None:
        self.rank = [1] * node_count
        self.parents = list(range(node_count))
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
            return
        elif self.rank[pv] > self.rank[pu]:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv
        else:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
        self.size -= 1


class Solution:
    def countComponents(self, node_count: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, dsu
        DSU
        """
        dsu = DSU(node_count)
        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.size