class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Integer = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        Roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        ans = ""
        index = 0
        while(num > 0):
            if (num >= Integer[index]):
                num = num - Integer[index]
                ans = ans + Roman[index]
            else:
                index = index + 1
        return ans
#Runtime: 20 ms, faster than 99.51% of Python online submissions for Integer to Roman.
#Memory Usage: 11.7 MB, less than 54.29% of Python online submissions for Integer