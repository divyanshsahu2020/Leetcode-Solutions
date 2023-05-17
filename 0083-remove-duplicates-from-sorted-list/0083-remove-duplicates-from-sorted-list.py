# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if(head==None):
            return head
        if(head.next==None):
            return head
        pre=head
        curr=pre.next
        while curr!=None and pre!=None:
            if(curr.val==pre.val):
                pre.next=curr.next
                curr=curr.next
                continue
            pre=curr
            curr=curr.next
        return head

