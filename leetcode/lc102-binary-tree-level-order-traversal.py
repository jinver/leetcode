# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        from collections import deque
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        result = []
        while len(queue) > 0:
            # print(queue)
            curr, level = queue.popleft()
            print(curr.val, level)
            if len(result) == level:
                # assume current level has not been created
                result.append([curr.val])
            elif len(result) > level:
                result[level].append(curr.val)
            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))
        return result
        