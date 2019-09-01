class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if ((nums[i] + nums[j]) == target):
                    List = []
                    List.append(i)
                    List.append(j)
                    return List
#Runtime: 4776 ms, faster than 22.23% of Python online submissions for Two Sum.
#Memory Usage: 12.6 MB, less than 75.68% of Python online submissions for Two Sum.
#Time:O(n^2) Space:O(1)