class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return (nums.index(target))
        else:
            return -1
#Runtime: 16 ms, faster than 99.48% of Python online submissions for Search in Rotated Sorted Array.
#Memory Usage: 11.8 MB, less than 93.88% of Python online submissions for Search in Rotated Sorted Array.