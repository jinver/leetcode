# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent.


class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        self.dfs(digits, dic, 0, '', res)
        return res

    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for char in dic[digits[index]]:
            self.dfs(digits, dic, index+1, path+char, res)

digits = '27'
s = Solution().letterCombinations(digits)
print(s)
