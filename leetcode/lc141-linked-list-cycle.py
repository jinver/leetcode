# Given a linked list, determine if it has a cycle in it.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dict = {}
        while head:
            if head in dict:
                return True
            dict[head] = True
            head = head.next
        return False