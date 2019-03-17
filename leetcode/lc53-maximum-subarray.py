# Given an integer array nums, find the contiguous subarray (containing at least one number) which 
# has the largest sum and return its sum.


class Solution:
    def maxSubArray(self, nums) -> int:
        high = nums[0]
        prev_sum = 0
        for i in range(len(nums)):
            if prev_sum > 0:
                curr = prev_sum + nums[i]
            else:
                curr = nums[i]
            prev_sum = curr
            high = max(high, curr)
        return high
