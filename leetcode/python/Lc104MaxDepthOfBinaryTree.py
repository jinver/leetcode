# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque()
        queue.append((root, 1))
        maxDepth = 1
        while queue:
            curr, level = queue.popleft()
            maxDepth = max(maxDepth, level)
            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))
        return maxDepth
        