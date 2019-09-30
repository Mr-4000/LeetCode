# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = head
        while (head!=None)and(head.next!=None):
            if (head.next.val == head.val):
                head.next = head.next.next
            else:
                head = head.next
        return ans
#Runtime: 44 ms, faster than 91.27% of Python3 online submissions for Remove Duplicates from Sorted List.
#Memory Usage: 14 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.