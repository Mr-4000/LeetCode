class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        fl = 0
        for i in range(0,l//2+1):
            if (s[i] != s[l-i-1]):
                return(0)
        return(1)