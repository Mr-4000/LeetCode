class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = []
        for i in range(0,n):
            frag = []
            for j in range(0,n):
                frag.append(matrix[n-j-1][i])
            print(frag)
            ans.append(frag)
        for i in range(0,n):
            matrix[i] = ans[i]
#Runtime: 40 ms, faster than 82.95% of Python3 online submissions for Rotate Image.
#Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Rotate Image.