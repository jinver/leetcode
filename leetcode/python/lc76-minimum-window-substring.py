# Given a string S and a string T, find the minimum window in S which will contain all the 
# characters in T in complexity O(n).


import sys

class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        left = 0
        right = 0
        dict = {}
        # build our initial count dict
        for c in t:
            if c in dict:
                dict[c] -= 1
            else:
                dict[c] = -1
        best = sys.maxsize
        best_left = None
        best_right = None
        while right < len(s):
            if s[right] in dict:
                dict[s[right]] += 1
            if not self.validSubstring(dict):
                right += 1
            else:
                while self.validSubstring(dict):
                    if right-left < best:
                        best = right-left
                        best_left = left
                        best_right = right
                    if s[left] in dict:
                        dict[s[left]] -= 1
                    left += 1
                right += 1
        if best_left is None:
            return ''
        else:
            return s[best_left:best_right+1]

    def validSubstring(self, dict):
        for key, val in dict.items():
            if val < 0: return False
        return True
