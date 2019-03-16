# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        from heapq import heapify, heappush, heappop
        loop = True
        result = None
        head = None
        heap = []
        
        for index, item in enumerate(lists):
            if item is not None:
                heappush(heap, (item.val, index))
        
        while len(heap) > 0:
            # heap contains items from all list
            # print(heap)
            low, index = heappop(heap)
            # print(low, index)
            lists[index] = lists[index].next
            if lists[index] is not None:
                heappush(heap, (lists[index].val, index))
            new_node = ListNode(low)
            
            if result:
                result.next = new_node
                result = new_node
            else:
                result = new_node
                head = new_node
            
        return head