# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        root.next = head
        
        
        while head and head.next:
            a, b = head, head.next
            b.next, a.next = a, b.next
            prev.next = b
            prev = prev.next.next
            head = head.next
        
        
        return root.next
            
            
            