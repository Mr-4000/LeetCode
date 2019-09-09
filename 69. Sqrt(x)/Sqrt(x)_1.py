#简单的二分法开方
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        mid = (low + high) / 2
        while (low < (high-1)):
            if ((mid*mid)<x):
                low = mid
                mid = (low + high) / 2
            else:
                high = mid
                mid = (low + high) / 2
        if ((high*high)==x):
            return high
        else:
            return low
#Runtime: 16 ms, faster than 92.02% of Python online submissions for Sqrt(x).
#Memory Usage: 11.8 MB, less than 21.57% of Python online submissions for Sqrt(x).