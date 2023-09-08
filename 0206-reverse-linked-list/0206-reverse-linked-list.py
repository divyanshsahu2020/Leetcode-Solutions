# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rever(head):
            if not head:
                return None
            if(head.next==None):
                return head
            ll=rever(head.next)
            temp=ll
            while temp.next!=None:
                temp=temp.next
            temp.next=head
            head.next=None
            return ll
        return rever(head)