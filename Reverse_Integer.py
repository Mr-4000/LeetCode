class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        fl = 0
        if (x<0):
            fl = 1
            x= 0 - x
        while (x>0):
            ans = ans * 10 + x % 10
            x = x / 10
        if (fl==1):
            ans = 0 - ans
        if ((ans > 2147483647)or(ans < -2147483648)):
            return(0)
        return(ans)