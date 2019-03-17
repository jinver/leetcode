# Given a collection of intervals, merge all overlapping intervals.


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
    
#     def __repr__(self):
#         return '[{},{}]'.format(self.start, self.end)

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        intervals = sorted(intervals, key=lambda x: x.start)
        print(intervals)
        i, j = 0, 1
        while j < len(intervals):
            overlap = self.intervalsOverlap(intervals[i].start, intervals[i].end, intervals[j].start, intervals[j].end)
            if overlap:
                self.mergeInterval(i, j, intervals)
            else:
                i += 1
                j += 1
        return intervals

    def intervalsOverlap(self, a, b, c, d):
        if c <= b and d >= a: return True
        else: return False

    def mergeInterval(self, i, j, intervals):
        start = min(intervals[i].start, intervals[j].start)
        end = max(intervals[i].end, intervals[j].end)
        new = Interval(s=start, e=end)
        intervals.pop(j)
        intervals[i] = new
