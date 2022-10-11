# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(level,head):
            if head is None:
                return level
        
            return max(dfs(level + 1, head.left),dfs(level + 1, head.right))
        
        
        level = dfs(0,root)
        
        return level