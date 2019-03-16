# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        
        result = None
        head = None
        while l1 is not None or l2 is not None:
            if l1 is None:
                new_node = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                new_node = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                print('l1: {}'.format(l1.val))
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                print('l2: {}'.format(l2.val))
                new_node = ListNode(l2.val)
                l2 = l2.next
                
            if result:
                result.next = new_node
                result = result.next
            else:
                result = new_node
                head = result
        return head
            
        