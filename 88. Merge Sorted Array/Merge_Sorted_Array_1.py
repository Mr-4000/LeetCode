class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        for i in range(0,m):
            nums.append(nums1[i])
        for i in range(0,n):
            nums.append(nums2[i])
        print(nums)
        nums.sort()
        print(nums)
        for i in range(0,m+n):
            nums1[i] = nums[i]
#Runtime: 36 ms, faster than 98.49% of Python3 online submissions for Merge Sorted Array.
#Memory Usage: 13.9 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.