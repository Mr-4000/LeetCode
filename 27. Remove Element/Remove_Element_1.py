#收到26题启发，采用2pointer办法
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while (i<=j):
            if (nums[i]!=val):
                i = i + 1
            else:
                if (nums[j] == val):
                    j = j - 1
                else:
                    nums[i] = nums[j]
                    j = j - 1
        return i
#Runtime: 20 ms, faster than 63.75% of Python online submissions for Remove Element.
#Memory Usage: 11.6 MB, less than 94.34% of Python online submissions for Remove Element.
#这里全部选取了最好结果的值