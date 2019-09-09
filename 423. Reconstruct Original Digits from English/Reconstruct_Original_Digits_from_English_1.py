class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''zero one two three four five six seven eight nine
        six:x !
        zero:z
        three:r
        two:w
        four:u
        seven:s !
        five:v
        one:o
        eight:g !'''
        num = {'x':0,'z':0,'g':0,'w':0,'e':0,'r':0,'u':0,'s':0,'v':0,'o':0}
        ans = ""
        for i in range(0,len(s)):
            if (s[i] in num):
                num[s[i]] = num[s[i]] + 1
        for i in range(0,num['g']):
            ans = ans + "8"
            num['e'] = num['e'] - 1
        for i in range(0,num['x']):
            ans = "6" + ans
            num['s'] = num['s'] - 1
        for i in range(0,num['s']):
            ans = ans[:num['x']]+ "7" + ans[num['x']:]
            num['e'] = num['e'] - 2
            num['v'] = num['v'] - 1
        for i in range(0,num['v']):
            ans = "5" + ans
            num['e'] = num['e'] - 1
        for i in range(0,num['u']):
            ans = "4" + ans
            num['r'] = num['r'] - 1
            num['o'] = num['o'] - 1
        for i in range(0,num['z']):
            ans = "0" + ans
            num['r'] = num['r'] - 1
            num['o'] = num['o'] - 1
            num['e'] = num['e'] - 1
        for i in range(0,num['r']):
            ans = ans[:num['z']] + "3" + ans[num['z']:]
            num['e'] = num['e'] - 2
        for i in range(0,num['w']):
            ans = ans[:num['z']] + "2" + ans[num['z']:]
            num['o'] = num['o'] - 1
        for i in range(0,num['o']):
            ans = ans[:num['z']] + "1" + ans[num['z']:]
            num['e'] = num['e'] - 1
        for i in range(0,num['e']):
            ans = ans + "9"
        return ans
#Runtime: 138 ms, faster than 26.67% of Python online submissions for Reconstruct Original Digits from English.
#Memory Usage: 13.8 MB, less than 50.00% of Python online submissions for Reconstruct Original Digits from English.