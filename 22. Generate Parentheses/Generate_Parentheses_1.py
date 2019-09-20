class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
#Runtime: 36 ms, faster than 94.01% of Python3 online submissions for Generate Parentheses.
#Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.