# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        head = l
        fl = 0
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        while (1==1):
            if (fl == 1):
                l.next = l2
                break
            if (fl == 2):
                l.next = l1
                break
            if (l1.val < l2.val):
                l.next = l1
                l.next.val = l1.val
                l = l.next
                if (l1.next == None):
                    fl = 1
                else:
                    l1 = l1.next
            else:
                l.next = l2
                l.next.val = l2.val
                l = l.next
                if (l2.next == None):
                    fl = 2
                else:
                    l2 = l2.next
        return(head.next)
#Runtime: 40 ms, faster than 88.08% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.