class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        print(a)
        while ('' in a):
            a.remove('')
        print(a)
        if (a==[]):
            return 0
        return len(a[-1])
#Runtime: 36 ms, faster than 67.46% of Python3 online submissions for Length of Last Word.
#Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Length of Last Word.