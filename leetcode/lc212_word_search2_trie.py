# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
# cells are those horizontally or vertically neighboring. The same letter cell may not be used 
# more than once in a word.


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_word = True
    
    def search(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.is_word

    @classmethod
    def subTrieSearch(cls, root, char):
        if char in root.children:
            return root.children[char]
        else:
            return None


class Solution:
    def findWords(self, board, words):
        # create Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, trie.root, '', res)
        # print(res)
        return res


    def dfs(self, i, j, board, trie, path, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie.children:
            return
        else:
            char = board[i][j]
            if trie.children[char].is_word:
                word = path+char
                if word not in res:
                    res.append(word)
            board[i][j] = '#'
            self.dfs(i, j+1, board, trie.children[char], path+char, res)
            self.dfs(i+1, j, board, trie.children[char], path+char, res)
            self.dfs(i, j-1, board, trie.children[char], path+char, res)
            self.dfs(i-1, j, board, trie.children[char], path+char, res)
            board[i][j] = char




words = ['tea', 'ted', 'ten', 'tent', 'cat', 'cape']
board = [
  ['o','t','e','x'],
  ['d','e','a','t'],
  ['c','n','e','p'],
  ['a','t','c','a']
]
s = Solution().findWords(board, words)
print(s)
