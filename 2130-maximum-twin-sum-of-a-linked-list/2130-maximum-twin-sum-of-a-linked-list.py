# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        while head!=None:
            arr.append(head.val)
            head=head.next
        l1=0
        l2=len(arr)-1
        max_sum=0
        while l1<l2:
            if(arr[l1]+arr[l2]>max_sum):
                max_sum=arr[l1]+arr[l2]
            l1+=1
            l2-=1
        return(max_sum)


