# Given a binary tree, return the preorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preorderRecursive(root, result)
        return result
        
        
    def preorderRecursive(self, root, result):
        if root:
            result.append(root.val)
            if root.left:
                self.preorderRecursive(root.left, result)
            if root.right:
                self.preorderRecursive(root.right, result)
            
            