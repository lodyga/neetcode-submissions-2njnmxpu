class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: 
    *     DS: array
    *     A: Single-source DFS, cycle detection
    * @param {number} vertexCount
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(vertexCount, edges) {
      // Tree property: E == V - 1
        if (edges.length !== vertexCount - 1)
            return false

      const adjs = new Map();
      for (let vertex = 0; vertex < vertexCount; vertex++) {
         adjs.set(vertex, new Set());
      }

      for (const [u, v] of edges) {
         if (u === v)
            return false
         adjs.set(u, adjs.get(u).add(v));
         adjs.set(v, adjs.get(v).add(u));
      }
      const visited = Array(vertexCount).fill(false);

      const dfs = (vertex, prevVertex) => {
         if (visited[vertex])
            return false

         visited[vertex] = true;

         for (const adjVertex of adjs.get(vertex)) {
            if (
               adjVertex !== prevVertex &&
               !dfs(adjVertex, vertex)
            )return false
         }
         return true
      }
      // No cycles and connected.
      return dfs(0, -1) && visited.every(v => v == true)
   };
}


const validTree = new Solution().validTree;