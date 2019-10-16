class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fl = 0
        start = 0
        end = len(s) - 1
        s = s.lower()
        for i in range(start,end+1):
            if (s[i].isalnum()):
                fl = 1
        if (fl == 0):
            return 1
        while (start<end):
            while (not s[start].isalnum()):
                start = start + 1
            while (not s[end].isalnum()):
                end = end - 1
            if (s[start] == s[end]):
                start = start + 1
                end = end - 1
            else:
                return 0
        return 1
#Runtime: 40 ms, faster than 62.47% of Python online submissions for Valid Palindrome.
#Memory Usage: 15.7 MB, less than 5.88% of Python online submissions for Valid Palindrome.