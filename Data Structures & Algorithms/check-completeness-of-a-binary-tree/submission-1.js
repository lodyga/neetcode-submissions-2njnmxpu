/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */


/**
 * class TreeNode {
 *    constructor(val = null, left = null, right = null) {
 *       this.val = val
 *       this.left = left
 *       this.right = right
 *    };
 * }
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {boolean}
    */
   isCompleteTree(root) {
      const queue = new Queue([root]);
      let wasNull = false;

      while (queue.size()) {
         const node = queue.dequeue();

         if (wasNull && node !== null) {
            return false
         } else if (node === null) {
            wasNull = true;
            continue
         }

         queue.enqueue(node.left);
         queue.enqueue(node.right);
      }

      return true
   };
}