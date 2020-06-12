class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def pd(s):
            if (int(s)>255):
                return False
            if ((len(s)>1)and(s[0]=="0")):
                return False
            return True
        ans = []
        l = len(s)
        if (l>12):
            return ans
        for i in range(1,l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    s1 = s[0:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    if ((pd(s1))and(pd(s2))and(pd(s3))and(pd(s4))):
                        new = s1+"."+s2+"."+s3+"."+s4;
                        ans.append(new)
        return ans
#Runtime: 40 ms, faster than 10.04% of Python online submissions for Restore IP Addresses.
#Memory Usage: 11.6 MB, less than 100.00% of Python online submissions for Restore IP Addresses.