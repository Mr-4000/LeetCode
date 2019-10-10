# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(root,nums):
            n = len(nums) // 2
            nums1 = nums[:n]
            nums2 = nums[n+1:]
            if (nums1!=[]):
                n1 = len(nums1) // 2
                new = TreeNode(nums1[n1])
                root.left = new
                build(new,nums1)
            if (nums2!=[]):
                n2 = len(nums2) // 2
                new = TreeNode(nums2[n2])
                root.right = new
                build(new,nums2)
        if (nums == []):
            return(None)
        ans = root = TreeNode(nums[len(nums) // 2])
        build(root,nums)
        return(ans)
#Runtime: 84 ms, faster than 25.10% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
#Memory Usage: 16.1 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.