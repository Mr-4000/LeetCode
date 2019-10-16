class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        low = 9999
        for i in prices:
            if (i < low):
                low = i
            if ((i - low) > ans):
                ans = i - low
        return ans
#Runtime: 36 ms, faster than 99.49% of Python online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 12.5 MB, less than 64.22% of Python online submissions for Best Time to Buy and Sell Stock.