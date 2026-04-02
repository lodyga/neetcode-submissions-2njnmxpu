class DSU:
    def __init__(self, N) -> None:
        self.parents = list(range(N))
        self.rank = [1] * N

    def find(self, vertex: int) -> int:
        while vertex != self.parents[vertex]:
            self.parents[vertex] = self.parents[self.parents[vertex]]
            vertex = self.parents[vertex]
        return vertex
    
    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = self.parents[pu]
            self.parents[v] = self.parents[pu]
        else:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = self.parents[pv]
            self.parents[u] = self.parents[pv]

        return True


class Solution:
    def validTree(self, vertex_count: int, edges: list[list[int]]) -> bool:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V + E)
        Tags: 
            DS: array
            A: DSU, cycle detection
        """
        # Tree property: E == V - 1
        if len(edges) != vertex_count - 1:
            return False

        dsu = DSU(vertex_count)
        for u, v in edges:
            if dsu.union(u, v) is False:
                return False
        
        return True