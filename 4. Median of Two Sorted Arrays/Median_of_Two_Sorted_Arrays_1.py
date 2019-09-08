#python的特质，用sort就可以简单做完，很期待正确的办法
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if ((len(nums) % 2)==0):
            ans = (nums[len(nums)/2] + nums[len(nums)/2 - 1]) / 2.0
        else:
            ans = nums[len(nums)/2]
        return ans
#Runtime: 60 ms, faster than 99.26% of Python online submissions for Median of Two Sorted Arrays.
#Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Median of Two Sorted Arrays.