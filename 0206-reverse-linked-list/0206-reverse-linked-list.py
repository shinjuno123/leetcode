# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize rev with None
        rev = None
        
        # loop through the given linked list, concatenating each node with rev in reverse
        while head:
            head, rev, rev.next = head.next, head, rev
        
        
        
        # return rev
        # O(n)
        return rev