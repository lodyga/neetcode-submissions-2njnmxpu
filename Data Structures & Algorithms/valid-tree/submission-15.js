class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: 
    *     DS: array
    *     A: Single-source BFS, cycle detection
    * @param {number} vertexCount
    * @param {number[][]} edges
    * @returns {boolean}
    */
   validTree(vertexCount, edges) {
      // Tree property: E == V - 1
      if (edges.length !== vertexCount - 1)
         return false

      const adjVertices = new Map();
      for (let vertex = 0; vertex < vertexCount; vertex++) {
         adjVertices.set(vertex, new Set());
      }

      for (const [u, v] of edges) {
         if (u === v)
            return false
         adjVertices.set(u, adjVertices.get(u).add(v));
         adjVertices.set(v, adjVertices.get(v).add(u));
      }
      const visited = Array(vertexCount).fill(false);

      const bfs = () => {
         const queue = new Queue([[0, -1]]);

         while (queue.size()) {
            const [vertex, prev] = queue.dequeue();

            if (visited[vertex])
               return false
            visited[vertex] = true;

            for (const adjVertex of adjVertices.get(vertex)) {
               if (adjVertex !== prev)
                  queue.enqueue([adjVertex, vertex]);
            }
         }
         return true
      }
      // No cycles and connected.
      return bfs() && visited.every(v => v == true)
   };
}


const validTree = new Solution().validTree;