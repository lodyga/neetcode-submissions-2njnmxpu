"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for index in range(1, len(intervals)):
            prev_end = intervals[index - 1].end
            current_begin = intervals[index].start
            
            if prev_end > current_begin:
                return False
            
        return True