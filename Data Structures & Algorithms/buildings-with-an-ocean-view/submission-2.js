class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: greedy
    * @param {number[]} heights
    * @return {number[]}
    */
   findBuildings(heights) {
      const res = [heights.length - 1];

      for (let idx = heights.length - 2; idx > -1; idx--) {
         const height = heights[idx];

         if (height > heights[res[res.length - 1]]) {
            res.push(idx);
         }
      }

      return res.reverse()
   };
}