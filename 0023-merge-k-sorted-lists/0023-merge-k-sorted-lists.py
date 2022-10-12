# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = head = ListNode()
        Q = []
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(Q,(node.val,i,node))
        
        while Q:
            val ,idx, node = heapq.heappop(Q)
            head.next = node
            head = head.next
            node = node.next
            if node is not None:
                heapq.heappush(Q,(node.val,idx,node))
        
        
        return root.next