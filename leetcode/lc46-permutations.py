# Given a collection of distinct integers, return all possible permutations.


import copy

class Solution:
    def permute(self, nums):
        working = []
        answers = []
        self.findPermutations(nums, working, answers)
        return answers

    def findPermutations(self, start, working, answers):
        if not start:
            answers.append(working)
            return
        
        for i in range(len(start)):
            # print('i, start, working, answer', i, start, working, answers)
            tempStart = copy.deepcopy(start)
            tempWorking = copy.deepcopy(working)
            val = tempStart.pop(i)
            tempWorking.append(val)
            self.findPermutations(tempStart, tempWorking, answers)
