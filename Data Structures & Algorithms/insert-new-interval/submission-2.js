class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: intervals, greede
    * @param {number[][]} intervals
    * @param {number[]} newInterval
    * @return {number[][]}
    */
   insert(intervals, newInterval) {
      const mergedInervals = [];

      for (let index = 0; index < intervals.length; index++) {
         const start = intervals[index][0];
         const end = intervals[index][1];
         const newStart = newInterval[0];
         const newEnd = newInterval[1];

         if (newEnd < start) {
            mergedInervals.push(newInterval);
            mergedInervals.push(...intervals.slice(index,));
            return mergedInervals  // early exit
         } else if (newStart > end) {
            mergedInervals.push([start, end]);
         } else {
            newInterval = [
               Math.min(start, newStart),
               Math.max(end, newEnd)
            ];
         }
      }
      mergedInervals.push(newInterval);
      return mergedInervals
   };
}