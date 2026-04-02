class DSU {
   constructor(nodeCount) {
      this.rank = Array(nodeCount).fill(1);
      this.parents = Array.from({ length: nodeCount }, (_, node) => node);
      this.size = nodeCount;
   }

   find(node) {
      while (node !== this.parents[node]) {
         this.parents[node] = this.parents[this.parents[node]];
         node = this.parents[node];
      }
      return node
   }

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu === pv)
         return
      else if (this.rank[pu] >= this.rank[pv]) {
         this.rank[pu] += this.rank[pv];
         this.parents[pv] = pu;
      } else {
         this.rank[pv] += this.rank[pu];
         this.parents[pu] = pv;
      }
      this.size -= 1
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, dsu
    * DSU
    * @param {number} nodeCount
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(nodeCount, edges) {
      const dsu = new DSU(nodeCount);
      for (const [u, v] of edges) {
         dsu.union(u, v)
      }
      return dsu.size
   };
}