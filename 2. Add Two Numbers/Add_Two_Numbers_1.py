# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        up = 0
        m = (l1.val + l2.val)%10
        up = (l1.val + l2.val)/10
        l3 = ListNode(m)
        lans = l3
        while (((l1.next!=None)or(l2.next!=None))or(up!=0)):
            if (l1.next==None):
                l=ListNode(0)
                l1.next = l
            if (l2.next==None):
                l = ListNode(0)
                l2.next = l
            n = (l1.next.val + l2.next.val + up)%10
            up = (l1.next.val + l2.next.val + up)/10
            ln = ListNode(n)
            l3.next = ln
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        return lans
#Runtime: 56 ms, faster than 63.21% of Python online submissions for Add Two Numbers.
#Memory Usage: 11.9 MB, less than 14.71% of Python online submissions for Add Two Numbers.        