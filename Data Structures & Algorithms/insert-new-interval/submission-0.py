class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: intervals
        """
        merged_intervals = []

        for index, (start, end) in enumerate(intervals):
            new_start = new_interval[0]
            new_end = new_interval[1]
            
            if new_end < start:
                merged_intervals.append(new_interval)
                merged_intervals.extend(intervals[index:])
                return merged_intervals
            elif new_start > end:
                merged_intervals.append([start, end])
            else:
                new_interval[0] = min(start, new_start)
                new_interval[1] = max(end, new_end)

        merged_intervals.append(new_interval)
        return merged_intervals