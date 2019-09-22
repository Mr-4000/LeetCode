class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (target not in nums):
            return [-1,-1]
        a = nums.index(target)
        b = a
        while ((b<len(nums))and(nums[b]==target)):
            b = b + 1
        return [a,b-1]
#Runtime: 68 ms, faster than 78.02% of Python online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 12.9 MB, less than 94.12% of Python online submissions for Find First and Last Position of Element in Sorted Array.