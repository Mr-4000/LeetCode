class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(","]":"[","}":"{"}
        stack = []
        fl = 0
        for i in s:
            if ((i=="(")or(i=="[")or(i=="{")):
                stack.append(i)
            else:
                if ((stack!=[])and(stack[-1] == dic[i])):
                    stack.pop(-1)
                else:
                    fl = 1
                    break
        if (stack!=[]):
            fl = 1
        if fl:
            return 0
        else:
            return 1
#Runtime: 36 ms, faster than 78.00% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.