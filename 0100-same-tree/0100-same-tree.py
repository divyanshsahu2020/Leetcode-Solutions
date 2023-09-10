# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(root):
            if root==None:
                return [None]
            return [root.val]+preorder(root.left)+preorder(root.right)
        
        if(preorder(p)==preorder(q)):
            return True
        return False
        