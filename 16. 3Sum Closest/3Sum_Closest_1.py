#直接对3Sum程序进行小的修改，没有什么特别的地方，也就没有_2的程序了
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        close = 99999999
        while(i<len(nums)-2):
            if(nums[i]!=nums[i-1] or i==0):
                a=target-nums[i]
                left=i+1
                right=len(nums)-1
                while(left!=right):
                    t = abs(target-nums[i]-nums[left]-nums[right])
                    if (t < close):
                        ans = nums[i] + nums[left] + nums[right]
                        close = t
                    if(nums[left]+nums[right]>a):
                        right-=1
                    else:
                        left+=1
            i = i + 1
        return ans
#Runtime: 204 ms, faster than 21.46% of Python online submissions for 3Sum Closest.
#Memory Usage: 11.5 MB, less than 100.00% of Python online submissions for 3Sum Closest.
#震惊的是内存占用竟然是最低的