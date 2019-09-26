#not use the split function. use the simple while loop and save the time
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s)
        if (s==""):
            return 0
        while ((index>0)and(s[index-1]==" ")):
            index = index - 1
        while ((index>0)and(s[index-1]!=" ")):
            count = count + 1
            index = index - 1
        return count
#Runtime: 32 ms, faster than 89.98% of Python3 online submissions for Length of Last Word.
#Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Length of Last Word.