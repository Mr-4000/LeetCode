class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        for i in range(0,128):
            arr.append(0)
        max = 0
        temp = 0
        for i in range(0,len(s)):
            temp = temp + 1
            if (arr[ord(s[i])]!=0):
                a = arr[ord(s[i])]
                temp = temp - a
                for j in range(0,128):
                    arr[j] = arr[j] - a
                    if (arr[j] < 0):
                        arr[j] = 0
            if (max<temp):
                max = temp
            arr[ord(s[i])] = temp
        return(max)