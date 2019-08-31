#发现对2pointer方法掌握不佳，使用while经常会面对循环终止位置问题
#使用for去对整体进行一次遍历，把不为val的调到前面去，用前面的pointer来计数即可
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(0,len(nums)):
            if(nums[j]!=val):
                nums[i] = nums[j]
                i = i + 1
        return i
#Runtime: 12 ms, faster than 96.90% of Python online submissions for Remove Element.
#Memory Usage: 11.5 MB, less than 98.11% of Python online submissions for Remove Element.
#这里全部选取了多次跑的最好结果值，其实和用while的方法并没有很大的理论差距，都是O(N)