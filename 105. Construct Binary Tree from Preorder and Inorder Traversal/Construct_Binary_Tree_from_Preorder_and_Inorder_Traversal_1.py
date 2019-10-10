# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(root,preorder,inorder,pos):
            new = TreeNode(preorder[0])
            if (pos == 1):
                root.left = new
            else:
                root.right = new
            m = inorder.index(preorder[0])
            inorder1 = inorder[:m]
            inorder2 = inorder[m+1:]
            preorder1 = preorder[1:len(inorder1)+1]
            preorder2 = preorder[len(inorder1)+1:]
            if (preorder1 != []):
                build(new,preorder1,inorder1,1)
            if (preorder2 != []):
                build(new,preorder2,inorder2,2)
        if (preorder == []):
            return(None)
            exit(0)
        ans = root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        inorder1 = inorder[:m]
        inorder2 = inorder[m+1:]
        preorder1 = preorder[1:len(inorder1)+1]
        preorder2 = preorder[len(inorder1)+1:]
        if (preorder1 != []):
            build(root,preorder1,inorder1,1)
        if (preorder2 != []):
            build(root,preorder2,inorder2,2)
        return ans
#Runtime: 188 ms, faster than 41.48% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
#Memory Usage: 89.6 MB, less than 5.26% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.