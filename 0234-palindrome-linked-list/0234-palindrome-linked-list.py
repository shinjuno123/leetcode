# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            slow, prev, prev.next = slow.next, slow, prev
        
        
        if fast:
            slow = slow.next
        
        while prev and slow and prev.val == slow.val:
            prev, slow = prev.next, slow.next
        
        return not prev