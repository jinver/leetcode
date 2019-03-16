# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findAncestors(self, root, node):
        ancestors = []
        curr = root
        while curr:
            ancestors.append(curr)
            if node.val == curr.val: return ancestors
            elif node.val < curr.val: 
                curr = curr.left
            elif node.val > curr.val: 
                curr = curr.right
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors = self.findAncestors(root, p)
        q_ancestors = self.findAncestors(root, q)
        common = list(set(p_ancestors).intersection(q_ancestors))
        for i in common:
            if min(p.val, q.val) <= i.val <= max(p.val,q.val): return i
            