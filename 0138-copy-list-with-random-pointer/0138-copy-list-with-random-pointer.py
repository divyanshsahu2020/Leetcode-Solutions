"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        new_head=None
        curr=None
        mapping={}
        while temp:
            node=Node(temp.val)
            if(new_head==None):
                new_head=node
                curr=node
            else:
                curr.next=node
                curr=curr.next
            mapping[temp]=curr
            temp=temp.next
        

        old=head
        n=new_head
        while old:
            if(old.random==None):
                n.random=None
            else:
                n.random=mapping[old.random]
            old=old.next
            n=n.next
        return new_head 