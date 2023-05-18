# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,csum=0):
            if(root==None):
                return False
            csum+=root.val
            if(not root.left and not root.right):
                return csum==targetSum
            return dfs(root.left,csum) or dfs(root.right,csum)
        return dfs(root)
    
        