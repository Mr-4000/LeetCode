#最终将3Sum拆解为2Sum+X，2Sum可以先排序，然后再用收尾慢慢收缩的方式寻找target
#并且可以在寻找时剔除相同的left，right，时间复杂度因为O(N)。在3Sum中，则需要每个nums[]中的元素都作为X一次，因此O(N^2）
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        first=[]
        i=0
        while(i<len(nums)-2):
            if(nums[i]!=nums[i-1] or i==0):
                target=0-nums[i]
                left=i+1
                right=len(nums)-1
                while(left!=right):
                    if(nums[left]+nums[right]==target):
                        first.append([nums[i],nums[left],nums[right]])
                        while(left<right):
                            left+=1
                            if(nums[left]!=nums[left-1]):
                                break
                        while(right>left):
                            right-=1
                            if(nums[right]!=nums[right+1]):
                                break
                    elif(nums[left]+nums[right]>target):
                        right-=1
                    elif(nums[left]+nums[right]<target):
                        left+=1
            i+=1
        return first
#Runtime: 820 ms, faster than 39.25% of Python online submissions for 3Sum.
#Memory Usage: 15 MB, less than 36.54% of Python online submissions for 3Sum.