class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return(s)
        m = 2*numRows - 2
        ans = ""
        for i in range(0,numRows):
            for j in range(0,len(s)):
                if ((j%m == (i))or(j%m == (m-i))):
                    ans = ans + s[j]
        return(ans)