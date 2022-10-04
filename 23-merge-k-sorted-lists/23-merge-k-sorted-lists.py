# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        root = head = ListNode(None)
        
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(q,(node.val, i ,node))
        
        
        while q:
            node = heapq.heappop(q)
            idx = node[1]
            val = node[0]
            current_node = node[2]
            
            head.next = ListNode(val)
            head = head.next
            
            current_node = current_node.next
            
            if current_node:
                heapq.heappush(q,(current_node.val, idx, current_node))
        
    
            
        return root.next
        
        
        
        
        
        
        