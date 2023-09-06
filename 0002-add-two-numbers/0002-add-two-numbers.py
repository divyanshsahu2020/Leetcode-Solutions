# Definition for singly-linked list.
#class ListNode(object):
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum = 0
        carry = 0
        head = None
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            if (sum >= 10):
                carry = sum // 10
                sum = sum % 10

            else:
                carry = 0
            if (head == None):
                head = ListNode()
                t = head
                head.val = sum
                head.next = None
            else:
                temp = ListNode(sum)
                temp.next = None
                head.next = temp
                head = head.next
            l1 = l1.next
            l2 = l2.next

        if(l1!=None):
            while l1!=None:
                sum=l1.val+carry
                if(sum>=10):
                    carry=sum//10
                    sum=sum%10
                else:
                    carry=0
                

                temp = ListNode(sum)
                temp.next = None
                head.next = temp
                head = head.next
                l1=l1.next
        if(l2!=None):
            while l2!=None:
                sum=l2.val+carry
                if(sum>=10):
                    carry=sum//10
                    sum=sum%10
                else:
                    carry=0
                
                temp = ListNode(sum)
                temp.next = None
                head.next = temp
                head = head.next
                l2=l2.next
        if(carry!=0):
            temp = ListNode(carry)
            temp.next = None
            head.next = temp
            head = head.next

    
        
        return t





