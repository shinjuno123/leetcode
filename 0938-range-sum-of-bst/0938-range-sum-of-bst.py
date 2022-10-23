# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_ = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        def dfs(root):        
            if root:
                if root.val >= low and root.val <= high:
                    self.sum_ += root.val
                
                dfs(root.left)
                dfs(root.right)
        
        
        dfs(root)
        
        return self.sum_