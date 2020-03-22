# Given an array nums of n integers where n > 1,  return an array output such that output[i] 
# is equal to the product of all the elements of nums except nums[i].

from typing import List
from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = deque()
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            left.append(product)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            right.appendleft(product)
        result = []
        for i in range(len(nums)):
            leftProduct = 1
            rightProduct = 1
            if i >= 1:
                leftProduct = left[i-1]
            if i < len(nums)-1:
                rightProduct = right[i+1]
            result.append(leftProduct * rightProduct)
        return result
        
nums = [1,2,3,4]
res = Solution().productExceptSelf(nums)
print(res)

        
