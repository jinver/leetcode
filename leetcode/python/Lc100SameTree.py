# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pTree = self.bfs(p)
        qTree = self.bfs(q)
        if len(pTree) != len(qTree):
            return False
        for i in range(len(pTree)):
            if pTree[i] != qTree[i]:
                return False
        return True


    def bfs(self, root: TreeNode) -> List:
        if not root: return []
        queue = deque()
        queue.append(root)
        result = [root.val]
        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                result.append(curr.left.val)
            else:
                result.append('#')
            if curr.right:
                queue.append(curr.right)
                result.append(curr.right.val)
            else:
                result.append('#')
        return result