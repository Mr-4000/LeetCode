#把每个字母代表的数字解析，然后如果比自己身后的数字小就减去
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l = []
        ans = 0
        for i in range(0,len(s)):
            l.append(Roman[s[i]])
        for i in range(0,len(s)):
            if ((i == (len(s)-1))or(l[i] >= l[i+1])):
                ans = ans + l[i]
            else:
                ans = ans - l[i]
        return(ans)
#Runtime: 44 ms, faster than 47.45% of Python online submissions for Roman to Integer.
#Memory Usage: 11.7 MB, less than 56.45% of Python online submissions for Roman to Integer.