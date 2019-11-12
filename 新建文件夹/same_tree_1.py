# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if ((p==None)and(q==None)):
            return True
        if ((p==None)and(q!=None)):
            return False
        if ((p!=None)and(q==None)):
            return False
        if (p.val!=q.val):
            return False
        if (p.val == q.val):
            return (self.isSameTree(p.left,q.left))and(self.isSameTree(p.right,q.right))
#Runtime: 28 ms, faster than 97.06% of Python3 online submissions for Same Tree.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Same Tree.