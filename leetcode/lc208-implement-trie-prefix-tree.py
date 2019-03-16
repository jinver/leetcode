# Implement a trie with insert, search, and startsWith methods.


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

    def startsWith(self, prefix):
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True