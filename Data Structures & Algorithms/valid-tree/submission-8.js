class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking, dfs, recursion
    * @param {number} n
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(n, edges) {
      const adjs = new Map();
      for (let vertex = 0; vertex < n; vertex++) {
         adjs.set(vertex, new Set());
      }
      for (const [u, v] of edges) {
         if (u === v)
            return false
         adjs.set(u, adjs.get(u).add(v));
         adjs.set(v, adjs.get(v).add(u));
      }
      const visited = new Set();

      const dfs = (vertex, prevVertex) => {
         if (visited.has(vertex))
            return false

         visited.add(vertex);

         for (const adjVertex of adjs.get(vertex)) {
            if (
               adjVertex !== prevVertex &&
               !dfs(adjVertex, vertex)
            )return false
         }
         return true
      }
      return dfs(0, -1) && visited.size === n
   };
}
const validTree = new Solution().validTree;