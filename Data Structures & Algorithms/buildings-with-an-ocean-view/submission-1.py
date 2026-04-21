class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: iteration
        """
        stack = []

        for idx, height in enumerate(heights):
            while stack and stack[-1][0] <= height:
                stack.pop()

            stack.append((height, idx))

        return [idx for _, idx in stack]