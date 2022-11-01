# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(None)
        carry = 0
        
        while carry or l1 or l2:
            sum_ = 0
            
            if l1:
                sum_ += l1.val
                l1 = l1.next
            
            if l2:
                sum_ += l2.val
                l2 = l2.next
            
            if carry:
                sum_ += carry
            
            carry, val = divmod(sum_, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next