#Two Pointers Approach
#因为已经排好序，用i来控制最后结果数组长度，可以知道i是一定小于数组长度的
#所以用j去遍历数组，当j发现一个和i当前值不一样的时候，把该数据放进i所在的位置就好
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(0,len(nums)):
            if(nums[j]!=nums[i]):
                i = i + 1
                nums[i] = nums[j]
        return i+1
#Runtime: 68 ms, faster than 69.60% of Python online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 13.6 MB, less than 64.06% of Python online submissions for Remove Duplicates from Sorted Array.
#再度改进，第一个数字一定是会存在最终数组里面的，因此j可以从1开始去遍历，i也是如此
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1,len(nums)):
            if(nums[j]!=nums[i]):
                i = i + 1
                nums[i] = nums[j]
        return i+1
#Runtime: 64 ms, faster than 86.22% of Python online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 13.5 MB, less than 95.31% of Python online submissions for Remove Duplicates from Sorted Array.
#小小改进大大加大了超过的人数。