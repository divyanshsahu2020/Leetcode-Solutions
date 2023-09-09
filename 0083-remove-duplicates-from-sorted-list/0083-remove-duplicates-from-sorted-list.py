# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return
        pre=head
        curr=head.next
        while curr:
            if(pre.val==curr.val):
                pre.next=curr.next
            else:
                pre=curr
            curr=curr.next
        return head
        