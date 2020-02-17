# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the 
# sorted order, not the kth distinct element.


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappush, heappop
        for n in range(len(nums)):
            nums[n] = nums[n]*-1
        heapify(nums)
        for i in range(k):
            result = heappop(nums)
        return result * -1