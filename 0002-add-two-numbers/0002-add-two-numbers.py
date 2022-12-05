# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize carry with 0
        carry = 0
        # initialize root with ListNode(None)
        root = head = ListNode(None)
        
        # loop through the 2 numbers while l1 or l2 or carry exist
        while l1 or l2 or carry:
            sum_ = 0
            
            if l1:
                sum_ += l1.val
                l1 = l1.next
            
            if l2:
                sum_ += l2.val
                l2 = l2.next
                
            if carry:
                sum_ += carry
            
            
            # in each iteration, add l1 number to l2 number and to carry and devide the result with 10
            quotient, remainder = divmod(sum_,10)
            
            # then remainder is going to be one new result node and quotient will be a carry
            carry = quotient
            
            # splicing root and new result node
            head.next = ListNode(remainder)
            head = head.next
        
        
        
        # return root.next
        return root.next