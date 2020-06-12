#比较好想的暴力算法
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums)<3):
            return []
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = []
        if (nums[len(nums)-1]<0):
            return []
        while((i < len(nums)-2)and(nums[i]<=0)):
            t = 0 -nums[i] - nums[j]
            if (t in nums[i+1:j]):
                    new = [nums[i],t,nums[j]]
                    if ((new in ans)!=1):
                        ans.append(new)
            f = 0 - nums[i]
            if (nums[j] > (f//2)):
                j = j - 1
            else:
                i = i + 1
                j = len(nums) - 1
        return ans
#效率太低，O(n^3)的效率发生超时错误