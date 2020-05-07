from heapq import heapify, heappushpop, heappop, heappop
import math

def findThreeLargestNumbers(array):
    maxLen = 3
    minHeap = [-math.inf]*3
    heapify(minHeap)
    for i in array:
        if i > minHeap[0]:
            heappushpop(minHeap, i)
    
    result = []
    while minHeap:
        result.append(heappop(minHeap))
    print(result)
    return result


nums = [5,6,2,7,8]
findThreeLargestNumbers(nums)
