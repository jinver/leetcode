# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return None
        queue = deque()
        result = [root.val]
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                result.append(curr.left.val)
            else:
                result.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                result.append(curr.right.val)
            else:
                result.append(curr.right)
        print(result)
        return str(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        tree = data[1:-1]
        tree = tree.split(',')
        tree = deque(tree)
        root = TreeNode(tree.popleft())
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            nextNode = tree.popleft().strip()
            if nextNode != 'None':
                curr.left = TreeNode(nextNode)
                queue.append(curr.left)
            nextNode = tree.popleft().strip()
            if nextNode != 'None':
                curr.right = TreeNode(nextNode)
                queue.append(curr.right)
        return root


        
        
a = "[1,2,3,None,None,4,5]"
Codec().deserialize(a)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))