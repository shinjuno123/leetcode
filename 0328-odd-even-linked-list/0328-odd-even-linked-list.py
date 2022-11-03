# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        root = head
        even_root = even = head.next
        
        # connect odd indices together
        # connect even indices together
        while even and even.next:
            even_next_next = even.next.next
            
            head.next = head.next.next
            head = head.next
            
            even.next = even_next_next
            even = even.next
    

        head.next = even_root
        
        
        return root
        
        
        