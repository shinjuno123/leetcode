# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node, prev = None):
            if not node:
                return prev
            
            next_, node.next = node.next, prev
            
            return reverse(next_, node)
        
        
        
        return reverse(head)