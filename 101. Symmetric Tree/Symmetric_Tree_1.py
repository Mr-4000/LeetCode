# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def judge(a,b):
            if ((a == None)and(b == None)):
                return True
            if ((a == None)or(b == None)):
                return False
            return ((a.val == b.val)and(judge(a.left,b.right))and(judge(a.right,b.left)))
        return judge(root,root)
#Runtime: 32 ms, faster than 98.79% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 13.8 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.