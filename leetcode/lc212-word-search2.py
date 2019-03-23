# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where 
# "adjacent" cells are those horizontally or vertically neighboring. The same letter cell 
# may not be used more than once in a word.

class Solution:
    def findWords(self, board, words):
        res = []
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    self.dfs(i, j, board, 0, word, res)
        return res


    def dfs(self, i, j, grid, index, word, res):
        # print('i, j', i, j, index)
        # if index == len(word)-1 and grid[i][j] == word[index]:
        #     print('Found: ', word, index, i, j)
        #     res.append(word)
        #     return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[index]:
            return
        elif index == len(word)-1 and grid[i][j] == word[index]:
            # print('Found: ', word, index, i, j)
            if word not in res:
                res.append(word)
            return
        else:
            char = grid[i][j]
            grid[i][j] = '#'
            self.dfs(i, j+1, grid, index+1, word, res)
            self.dfs(i+1, j, grid, index+1, word, res)
            self.dfs(i, j-1, grid, index+1, word, res)
            self.dfs(i-1, j, grid, index+1, word, res)
            grid[i][j] = char


grid = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
s = Solution().findWords(grid, words)
print(s)