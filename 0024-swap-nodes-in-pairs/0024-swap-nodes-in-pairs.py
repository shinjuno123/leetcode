# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize root with empty linked list and concatenate it with head
        root = node = ListNode(None)
        root.next = head
        
        start, node = node, node.next
        # swap 2 adjacent nodes in each iteration until node reaches at the end of the Linked list
        while node and node.next:
            a, b = node, node.next
            b.next, a.next = a, b.next
            start.next = b
            start = start.next.next
            
            node = node.next
            
        
        
        
        # O(n)
        # return head
        return root.next