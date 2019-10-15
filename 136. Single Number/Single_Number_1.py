class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans
#Runtime: 100 ms, faster than 71.30% of Python3 online submissions for Single Number.
#Memory Usage: 16.3 MB, less than 6.56% of Python3 online submissions for Single Number.