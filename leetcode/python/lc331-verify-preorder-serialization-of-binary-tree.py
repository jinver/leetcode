# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null 
# node, we record the node's value. If it is a null node, we record using a sentinel value such as #.


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        n = 1
        s = preorder.split(',')
        for i in range(len(s)):
            n -= 1
            if n < 0:
                return False
            if s[i] != '#':
                n += 2
        if n == 0: return True
        else: return False
            