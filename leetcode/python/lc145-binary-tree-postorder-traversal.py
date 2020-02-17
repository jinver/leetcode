# Given a binary tree, return the postorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def peek_stack(stack):
        if stack:
            return stack[-1]
    
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        result, stack = [], []
        stack.append((root, False))
        while stack:
            curr, visited = stack.pop()
            if visited:
                result.append(curr.val)
            else:
                stack.append((curr, True))
                if curr.right:
                    stack.append((curr.right, False))
                if curr.left:
                    stack.append((curr.left, False))
        return result