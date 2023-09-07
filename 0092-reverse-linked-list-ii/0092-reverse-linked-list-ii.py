# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        arr=[0]
        temp=head
        while temp:
            arr.append(temp)
            temp=temp.next
        while left<right:
            arr[left].val,arr[right].val=arr[right].val,arr[left].val
            left+=1
            right-=1
        temp=head
        return arr[1]
