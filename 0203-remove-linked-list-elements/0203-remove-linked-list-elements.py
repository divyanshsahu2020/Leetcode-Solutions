# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        pre=dummy
        curr=head
        while curr:
            if(curr.val==val):
                pre.next=curr.next
            else:
                pre=curr
            curr=curr.next
        return dummy.next
            