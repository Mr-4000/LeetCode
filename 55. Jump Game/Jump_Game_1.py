class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        target = n-1
        for i in range(n-2,-1,-1):
            if (nums[i] + i >= target):
                target = i
        if (target==0):
            return 1
        else:
            return 0
#Runtime: 52 ms, faster than 100.00% of Python online submissions for Jump Game.
#Memory Usage: 13.2 MB, less than 85.71% of Python online submissions for Jump Game.