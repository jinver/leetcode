# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.


class NumArray:
    def __init__(self, nums):
        self.sums = self.calcSum(nums)

    def calcSum(self, nums):
        result = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            result.append(sum)
        return result

    def sumRange(self, i: int, j: int) -> int:
        if i == 0: return self.sums[j]
        else: return self.sums[j] - self.sums[i-1]
