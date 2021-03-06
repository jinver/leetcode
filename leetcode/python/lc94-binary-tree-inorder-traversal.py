# Given a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        stack = []
        result = []
        curr = root
                
                
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0: break
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        return result
        
        
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.inorderDfsRecursive(root, result)
        return result
        
    def inorderRecursive(self, root, result):
        if root:
            if root.left:
                self.inorderDfsRecursive(root.left, result)
            result.append(root.val)
            if root.right:
                self.inorderDfsRecursive(root.right, result)
            
            
        
        