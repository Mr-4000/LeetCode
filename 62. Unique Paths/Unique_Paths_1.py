class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0]*m] * n
        for i in range(0,m):
            ans[0][i] = 1
        for i in range(0,n):
            ans[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return(ans[n-1][m-1])
#Runtime: 40 ms, faster than 43.22% of Python3 online submissions for Unique Paths.
#Memory Usage: 13.8 MB, less than 5.77% of Python3 online submissions for Unique Paths.