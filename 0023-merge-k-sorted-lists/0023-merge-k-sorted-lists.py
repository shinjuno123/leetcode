# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:    
        Q = []
        head = root = ListNode(None)
        for i, n in enumerate(lists):
            if n is not None:
                heapq.heappush(Q,(n.val,i,n))
        
        
        while Q:
            value, index, node = heapq.heappop(Q)
            head.next = node
            head = head.next
            node = node.next
            if node is not None:
                heapq.heappush(Q,(node.val,index,node))
            
            
        return root.next