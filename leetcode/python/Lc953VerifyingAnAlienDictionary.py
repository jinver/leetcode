

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for index, char in enumerate(order):
            orderDict[char] = index

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            isInOrder = self.compareTwoWords(word1, word2, orderDict)
            if isInOrder == False:
                return False
        return True


    def compareTwoWords(self, word1, word2, orderDict):
        if len(word1) <= len(word2):
            shorter = word1
        else:
            shorter = word2
        for i in range(len(shorter)):
            if word1[i] != word2[i]:
                if orderDict[word1[i]] < orderDict[word2[i]]:
                    return True
                else:
                    return False
        if shorter == word1:
            return True
        else: 
            return False


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
result = Solution().isAlienSorted(words, order)
print(result)
