# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        l = []
        index = 0
        def make(a,index,l):
            if (a == None):
                return
            if (index >= len(l)):
                l.append([])
            l[index].append(a.val)
            make(a.left,index+1,l)
            make(a.right,index+1,l)
        make(root,index,l)
        return(l)
#Runtime: 36 ms, faster than 95.67% of Python3 online submissions for Binary Tree Level Order Traversal.
#Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.