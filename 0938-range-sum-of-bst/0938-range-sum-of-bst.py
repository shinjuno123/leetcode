# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):        
            if root:
                if root.val < low:
                    return dfs(root.right)
                elif root.val > high:
                    return dfs(root.left)
                print(root.val)
                return root.val + dfs(root.left) + dfs(root.right)
            else:
                return 0
        
        
        return dfs(root)