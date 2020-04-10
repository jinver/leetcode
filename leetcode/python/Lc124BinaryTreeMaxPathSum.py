# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution:
    def __init__(self):
        self.high = -sys.maxsize

    def maxPathSum(self, root) -> int:
        self.dfs(root)
        return self.high

    def dfs(self, root) -> int:
        if not root:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if not left: left = 0
        if not right: right = 0
        takeBoth = left + right + root.val
        takeOne = max(left, right) + root.val
        currHigh = max(takeBoth, takeOne, root.val)
        self.high = max(self.high, currHigh)
        return max(takeOne, root.val)




res = Solution().maxPathSum(None)