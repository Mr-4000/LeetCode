#就像2Sum->3Sum一样，加一层外部循环，3Sum->4Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if (len(nums) < 4):
            return []
        ans = []
        for d in range(len(nums)-1,2,-1):
            a = 0
            while (a < (d-2)):
                n_target = target - nums[a] - nums[d]
                b = a + 1
                c = d - 1
                while (b < c):
                    if ((nums[b] + nums[c])==n_target):
                        new = [nums[a],nums[b],nums[c],nums[d]]
                        if ((new in ans)!=1):
                            ans.append(new)
                    if ((nums[b] + nums[c]) < n_target):
                        b = b + 1
                    else:
                        c = c - 1
                a = a + 1
        return ans
#Runtime: 796 ms, faster than 40.73% of Python online submissions for 4Sum.
#Memory Usage: 11.7 MB, less than 90.91% of Python online submissions for 4Sum.
#没有4Sum_2