# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    left_t = 0
    right_t = 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balance(root):
            if not root:
                return -1
        
            
            left = balance(root.left)
            right = balance(root.right)
            
            if abs(self.right_t - self.left_t) >= 2:
                return -1
            
            self.left_t = left
            self.right_t = right

            
            return max(left, right) + 1
        
        balance(root)
 
        return abs(self.right_t - self.left_t) < 2 