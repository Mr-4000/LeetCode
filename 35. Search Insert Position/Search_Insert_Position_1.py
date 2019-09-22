class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (target in nums):
            return nums.index(target)
        left = 0
        right = len(nums)
        mid = (left + right) // 2
        if (nums[len(nums) - 1] < target):
            return len(nums)
        if (nums[0] > target):
            return 0
        while (left<right):
            if ((nums[mid-1]<target)and(nums[mid]>target)):
                return mid
            if (nums[mid] < target):
                left = mid
            if (nums[mid] > target):
                right = mid
            mid = (left + right) // 2
#Runtime: 36 ms, faster than 62.81% of Python online submissions for Search Insert Position.
#Memory Usage: 12.3 MB, less than 56.14% of Python online submissions for Search Insert Position.