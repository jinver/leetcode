# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        prefix = ''
        shortest = None
        for word in strs:
            if shortest is None:
                shortest = word
            else:
                if len(word) < len(shortest):
                    shortest = word
        i = 0
        if shortest is None:
            return prefix
        if len(shortest) == 0:
            return prefix
        while i < len(shortest):
            for word in strs:
                if word[i] != shortest[i]:
                    return prefix
            prefix += shortest[i]
                
            i += 1
        return prefix