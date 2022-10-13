# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(head):
            if head is None:
                return 0
            
            left = dfs(head.left)
            right = dfs(head.right)
            
            if head.left and head.left.val == head.val:
                left += 1
            else:
                left = 0
            
            if head.right and head.right.val == head.val:
                right += 1
            else:
                right = 0
            
            self.result = max(self.result, left + right)
            
            return max(left, right)
        
        dfs(root)
        
        return self.result
        