# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        l=0
        r=0
        if(root.left):
            l=Solution.maxDepth(self,root.left)
        if(root.right):
            r=Solution.maxDepth(self,root.right)
        return 1+max(l,r)
        
        