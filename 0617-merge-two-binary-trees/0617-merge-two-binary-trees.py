# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        head1, head2 = root1, root2
        # new_tree = TreeNode(None)
        
        def dfs(head1, head2):
            if head1 is None and head2 is None:
                return None
            
            if head1 is None and head2:
                return head2
            
            if head1 and head2 is None:
                return head1
            
            head1.left = dfs(head1.left, head2.left)
            head1.right = dfs(head1.right, head2.right)
            
            head1.val += head2.val
            
            return head1
             
    
        
        
        return dfs(head1,head2)