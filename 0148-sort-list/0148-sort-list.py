# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self,l1,l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1,l2 = l2,l1
            l1.next = self.mergeSort(l1.next, l2)
        
        return l1 or l2
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        slow, fast, half = head, head, None
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        
        half.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeSort(l1,l2)
        
        
        