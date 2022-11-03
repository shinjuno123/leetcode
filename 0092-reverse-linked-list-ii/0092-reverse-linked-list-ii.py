# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(None)
        root.next = head
        
        for _ in range(left - 1):
            start = start.next
        
        node = start.next
        
        for _ in range(right - left):
            tmp = start.next
            end = node.next
            node.next, end.next = end.next, tmp
            start.next = end
        
        return root.next