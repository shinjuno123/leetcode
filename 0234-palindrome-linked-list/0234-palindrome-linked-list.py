# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # initialize slow and fast with head
        # initialize rev with None
        slow = fast = head
        rev = None
        
        # loop through the linked list until slow reaches at the middle of the linked list and fast reaches at the end of it
        # in each iteration, concatenate rev with slow in reverse
        while fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next ,slow, rev
            
            
        
        # if fast exists, move slow   
        if fast:
            slow = slow.next
        
        # check if rev and slow are same
        while rev and slow and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        
        
        # if rev is at end of the linked list then, it is palindrome
        return not rev
        
        
        
        