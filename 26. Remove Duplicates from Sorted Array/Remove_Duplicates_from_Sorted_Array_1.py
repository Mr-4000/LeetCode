class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        index = 0
        while (index<(len(nums)-1)):
            if (nums[index]==nums[index+1]):
                nums.pop(index+1)
            else:
                index = index + 1
        return (index+1)
#Runtime: 88 ms, faster than 17.33% of Python online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 13.6 MB, less than 56.25% of Python online submissions for Remove Duplicates from Sorted Array.