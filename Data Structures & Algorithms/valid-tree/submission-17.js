class DSU {
   constructor(N) {
      this.parents = Array.from({ length: N }, (_, index) => index);
      this.rank = Array(N).fill(1);
   };

   find(vertex) {
      while (vertex !== this.parents[vertex]) {
         this.parents[vertex] = this.parents[this.parents[vertex]];
         vertex = this.parents[vertex];
      }
      return vertex
   };

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu == pv) {
         return false
      } else if (this.rank[pu] >= this.rank[pv]) {
         this.rank[pu] += this.rank[pv];
         this.parents[pv] = this.parents[pu];
         this.parents[v] = this.parents[pu];
      } else {
         this.rank[pv] += this.rank[pu];
         this.parents[pu] = this.parents[pv];
         this.parents[u] = this.parents[pv];
      }
      return true
   };
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: 
    *     DS: array
    *     A: DSU, cycle detection
    * @param {number} vertexCount
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(vertexCount, edges) {
      // Tree property: E == V - 1
      if (edges.length !== vertexCount - 1)
         return false

      const dsu = new DSU(vertexCount);
      for (const [u, v] of edges)
         if (dsu.union(u, v) === false)
            return false

      return true
   };
}


const validTree = new Solution().validTree;