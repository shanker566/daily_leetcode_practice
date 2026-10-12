import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # 1. Push the head of each non-empty list into the min-heap.
        # Include the list index 'i' to handle duplicate values safely.
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
                
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Extract the minimum node and push its next element into the heap
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
