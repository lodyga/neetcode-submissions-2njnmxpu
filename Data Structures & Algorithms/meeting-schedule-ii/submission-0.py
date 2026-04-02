"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals):
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: intervals, heap
        """
        intervals.sort(key=lambda x: x.start)
        rooms = []  # [end, ...]

        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)

        return len(rooms)