class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, dsu
    * DFS
    * @param {number} nodeCount
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(nodeCount, edges) {
      const adjs = new Map();
      for (let node = 0; node < nodeCount; node++) {
         adjs.set(node, new Set());
      }
      for (const [u, v] of edges) {
         adjs.set(u, adjs.get(u).add(v));
         adjs.set(v, adjs.get(v).add(u));
      }
      const visited = new Set();
      let components = 0;
      const dfs = (node) => {
         if (visited.has(node))
            return

         visited.add(node);

         for (const adjNode of adjs.get(node))
            dfs(adjNode);
      };
      for (let node = 0; node < nodeCount; node++) {
         if (!visited.has(node)) {
            dfs(node)
            components++;
         }
      }
      return components
   };
}