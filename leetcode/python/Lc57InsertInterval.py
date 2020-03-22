# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.


from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        result = []
        i = 0
        while i < len(intervals):
            if self.hasOverlap(intervals[i], newInterval):
                newInterval = self.mergeOverlap(intervals[i], newInterval)
            else: # no overlap
                if newInterval[1] < intervals[i][0]:
                    break
                result.append(intervals[i])
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result
    
    def hasOverlap(self, interval1, interval2):
        if (interval2[0] <= interval1[1] and interval2[1] >= interval1[0]) or \
            (interval2[1] >= interval1[0] and interval2[0] <= interval1[1]):
            return True
        else:
            return False
    
    def mergeOverlap(self, interval1, interval2):
        start = min(interval1[0], interval2[0])
        end = max(interval1[1], interval2[1])
        return [start, end]


intervals = [[1,5]]
newInterval = [2,3]
res = Solution().insert(intervals, newInterval)
print(res)