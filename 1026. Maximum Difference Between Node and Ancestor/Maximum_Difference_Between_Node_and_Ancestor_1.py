# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def f(root,min,max):
            ans = 0
            if (root == None):
                return (max - min)
            if (root.val < min):
                min = root.val
            if (root.val > max):
                max = root.val
            l = f(root.left,min,max)
            r = f(root.right,min,max)
            if (ans<l):
                ans = l
            if (ans<r):
                ans = r
            return ans
        return f(root,root.val,root.val)
#Runtime: 20 ms, faster than 94.04% of Python online submissions for Maximum Difference Between Node and Ancestor.
#Memory Usage: 18.6 MB, less than 25.00% of Python online submissions for Maximum Difference Between Node and Ancestor.