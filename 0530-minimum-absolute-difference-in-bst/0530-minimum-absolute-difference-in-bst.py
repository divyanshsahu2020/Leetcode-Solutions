# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        if(root==None):
            return
        def traversal(root):
            if(root==None):
                return 
            arr.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        arr.sort()
        print(arr)
        diff=999999
        l=0
        while l<len(arr)-1:
            if((arr[l+1]-arr[l])<diff):
                diff=arr[l+1]-arr[l]
            l+=1
        return(diff)



        