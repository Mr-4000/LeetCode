#简单的二进制加法思路
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = "0" + a
        b = "0" + b
        indexa = len(a) - 1
        indexb = len(b) - 1
        temp = 0
        ans = ""
        while ((indexa>0)or(indexb>0)):
            if ((int(a[indexa]) + int(b[indexb]) + temp)==0):
                ans = "0" + ans
                temp = 0
                if (indexa != 0):
                    indexa = indexa - 1
                if (indexb != 0):
                    indexb = indexb - 1
            else:
                if ((int(a[indexa]) + int(b[indexb]) + temp)==1):
                    ans = "1" + ans
                    temp = 0
                    if (indexa != 0):
                        indexa = indexa - 1
                    if (indexb != 0):
                        indexb = indexb - 1
                else:
                    if ((int(a[indexa]) + int(b[indexb]) + temp)==2):
                        ans = "0" + ans
                        temp = 1
                        if (indexa != 0):
                            indexa = indexa - 1
                        if (indexb != 0):
                            indexb = indexb - 1
                    else:
                        ans = "1" + ans
                        temp = 1
                        if (indexa != 0):
                            indexa = indexa - 1
                        if (indexb != 0):
                            indexb = indexb - 1
        if (temp==1):
            ans = "1" + ans
        return(ans)
#Runtime: 24 ms, faster than 57.70% of Python online submissions for Add Binary.
#Memory Usage: 11.7 MB, less than 65.79% of Python online submissions for Add Binary.