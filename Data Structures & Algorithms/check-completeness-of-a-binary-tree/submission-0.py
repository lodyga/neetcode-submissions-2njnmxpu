# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        queue = deque([root])
        was_none = False

        while queue:
            node = queue.popleft()

            if was_none and node is not None:
                return False

            elif node is None:
                was_none = True
                continue

            queue.append(node.left)
            queue.append(node.right)

        return True