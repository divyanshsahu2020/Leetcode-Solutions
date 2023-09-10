# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root==None:
                return 0
            return 1+max(height(root.left),height(root.right))

        if(root==None):
            return True
        l=Solution.isBalanced(self,root.left)
        r=Solution.isBalanced(self,root.right)
        if(l and r):
            return abs(height(root.left)-height(root.right))<=1
        return False
        
        