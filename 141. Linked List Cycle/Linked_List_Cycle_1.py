# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while (head!=None):
            if (head.val > int(head.val)):
                return 1
            head.val = head.val + 0.1
            head = head.next
        return 0
#Runtime: 60 ms, faster than 46.55% of Python3 online submissions for Linked List Cycle.
#Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.