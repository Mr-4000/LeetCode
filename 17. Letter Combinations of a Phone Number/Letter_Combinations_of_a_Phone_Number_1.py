class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        ans = [""]
        temp = []
        if (digits==""):
            return []
        for i in range(0,len(digits)):
            n = int(digits[i])
            for k in phone[n]:
                for m in ans:
                    temp.append(m+k)
            ans = temp
            temp = []
        return ans
#Runtime: 36 ms, faster than 73.65% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.