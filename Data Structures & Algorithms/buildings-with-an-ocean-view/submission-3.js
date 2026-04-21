class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: monotonic increasing stack
    *     A: iteration
    * @param {number[]} heights
    * @return {number[]}
    */
   findBuildings(heights) {
      const stack = [];

      for (let idx = 0; idx < heights.length; idx++) {
         const height = heights[idx];

         while (stack.length && stack[stack.length - 1][0] <= height) {
            stack.pop();
         }

         stack.push([height, idx]);
      }

      return stack.map(([, idx]) => idx)
   };
}