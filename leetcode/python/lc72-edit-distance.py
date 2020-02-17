# Given two words word1 and word2, find the minimum number of operations required to convert 
# word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character


class Solution:
    def initialize_score(self, score):
        y = score[0]
        for i in range(len(y)):
            # print(i)
            score[0][i] = i

        for x in range(len(score)):
            for y in range(len(score[x])):
                score[x][0] = x

    def match(self, a, b):
        if a == b: return 0
        else: return 1

    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        score = [[0 for x in range(len(word2)+1)] for y in range(len(word1)+1)]
        self.initialize_score(score)

        for x in range(1, len(score)):
            for y in range(1, len(score[x])):
                diag = score[x-1][y-1] + self.match(word1[x-1], word2[y-1])
                up = score[x][y-1] + 1
                left = score[x-1][y] + 1
                best = min(diag, up, left)
                score[x][y] = best
        return score[-1][-1]