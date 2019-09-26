class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1,2]
        for i in range(2,n):
            ans.append(ans[i-1] + ans[i-2])
        return(ans[n-1])
#Runtime: 16 ms, faster than 68.13% of Python online submissions for Climbing Stairs.
#Memory Usage: 11.8 MB, less than 32.81% of Python online submissions for Climbing Stairs.