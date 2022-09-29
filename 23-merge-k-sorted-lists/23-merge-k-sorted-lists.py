# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []
        
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next:
                heapq.heappush(heap,(result.next.val,idx,result.next))
        
        
        return root.next
            
        
        
            
            
            
            
            
            