# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        a = head
        while (a.next!=None):
            count = count + 1
            print("*")
            a = a.next
        a = head
        if (n == (count+1)):
            return head.next
        for i in range(0,count - n):
            a = a.next
        a.next = a.next.next
        return(head)
#Runtime: 44 ms, faster than 22.50% of Python3 online submissions for Remove Nth Node From End of List.
#Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.