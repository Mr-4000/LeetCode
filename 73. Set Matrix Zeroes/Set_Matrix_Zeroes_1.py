class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matmap = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if (matrix[i][j]==0):
                    matmap.append([i,j])
        #print(matmap)
        for i in matmap:
            for j in range(0,len(matrix[0])):
                matrix[i[0]][j] = 0
            for j in range(0,len(matrix)):
                matrix[j][i[1]] = 0
        return matrix
#Runtime: 156 ms, faster than 57.92% of Python3 online submissions for Set Matrix Zeroes.
#Memory Usage: 14.4 MB, less than 5.13% of Python3 online submissions for Set Matrix Zeroes.