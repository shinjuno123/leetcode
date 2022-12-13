# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # heights when node reaches at the end of tree
        # save the heights at the end of the tree
        # and check if max_height - min_height is smaller than 2

        def check(head):
            if not head:
                return 0
            
            left = check(head.left)
            right = check(head.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        
        return check(root) != -1
