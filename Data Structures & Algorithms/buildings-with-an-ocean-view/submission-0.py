class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: greedy
        """
        res = [len(heights) - 1]

        for idx in range(len(heights) - 2, - 1, -1):
            height = heights[idx]

            if height > heights[res[-1]]:
                res.append(idx)

        return res[::-1]