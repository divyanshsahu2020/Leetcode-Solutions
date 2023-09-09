# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        res=0
        for i in range(len(arr)-1,-1,-1):
            temp=len(arr)-1-i
            if(temp>0):
                res=max(res,arr[i]+arr[temp])
        return res    