class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        now = -1
        fl = 0
        i = 0
        while(i<len(nums)):
            if (nums[i] == now):
                if (fl == 0):
                    fl = 1
                    i = i + 1
                else:
                    del nums[i]
            else:
                fl = 0
                now = nums[i]
                i = i + 1
#Runtime: 68 ms, faster than 39.34% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for Remove Duplicates from Sorted Array II.