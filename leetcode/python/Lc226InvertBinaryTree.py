# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left:
                queue.append(curr.left)
            if curr.right:  
                queue.append(curr.right)
        return root