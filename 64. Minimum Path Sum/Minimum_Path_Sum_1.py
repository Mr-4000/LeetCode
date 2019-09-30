class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        path = []
        for i in range(0,m+1):
            frag = []
            for j in range(0,n+1):
                frag.append(9999)
            path.append(frag)
        path[0][1] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                path[i][j] = grid[i-1][j-1] + min(path[i-1][j],path[i][j-1])
        return path[m][n]
#Runtime: 112 ms, faster than 77.44% of Python3 online submissions for Minimum Path Sum.
#Memory Usage: 15.2 MB, less than 26.32% of Python3 online submissions for Minimum Path Sum.