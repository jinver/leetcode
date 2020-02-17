# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a 
# function to search target in nums. If target exists, then return its index, otherwise return -1.


class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        left = 0
        right = len(nums) - 1
        while True:
            curr = int((left + right) / 2)
            if left == right:
                if target == nums[curr]: return curr
                else: return -1
            if target == nums[curr]:
                return curr
            elif target < nums[curr]:
                right = max(curr - 1, 0)
            else:
                left = curr + 1