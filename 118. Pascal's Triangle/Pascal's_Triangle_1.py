class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows == 0):
            return []
        if (numRows == 1):
            return [[1]]
        ans = [[1]]
        for i in range(1,numRows):
            ans.append([1,1])
            for j in range(1,i):
                new = ans[i-1][j-1]+ans[i-1][j]
                ans[i].insert(j,new)
        return(ans)
#Runtime: 36 ms, faster than 76.35% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.