# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        queue = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(queue,(lists[i].val, i, lists[i]))
                
        
        while queue:
            node = heapq.heappop(queue)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next:
                heapq.heappush(queue, (result.next.val, idx, result.next))
                
        
        return root.next
        
            
            
            
            
            
            