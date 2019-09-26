class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (matrix==[]):
            return []
        m = len(matrix)
        n = len(matrix[0])
        f = []
        ans = []
        t = 1
        for i in range(0,m):
            frag = []
            for j in range(0,n):
                frag.append(0)
            f.append(frag)
        x=0
        y=0
        ans.append(matrix[0][0])
        f[0][0]=1
        print(m,n)
        for i in range(1,m*n):
            if (t==1):
                if ((y+1<n)and(f[x][y+1]!=1)):
                    ans.append(matrix[x][y+1])
                    f[x][y+1] = 1
                    y = y + 1
                else:
                    ans.append(matrix[x+1][y])
                    f[x+1][y] = 1
                    x = x + 1
                    t = 2
                    continue
            if (t==2):
                if ((x+1<m)and(f[x+1][y]!=1)):
                    ans.append(matrix[x+1][y])
                    f[x+1][y] = 1
                    x = x + 1
                else:
                    ans.append(matrix[x][y-1])
                    f[x][y-1] = 1
                    y = y - 1
                    t = 3
                    continue
            if (t==3):
                if ((y-1>=0)and(f[x][y-1]!=1)):
                    ans.append(matrix[x][y-1])
                    f[x][y-1] = 1
                    y = y - 1
                else:
                    ans.append(matrix[x-1][y])
                    f[x-1][y]=1
                    x = x - 1
                    t = 4
                    continue
            if (t==4):
                if ((x-1>=0)and(f[x-1][y]!=1)):
                    ans.append(matrix[x-1][y])
                    f[x-1][y] = 1
                    x = x - 1
                else:
                    ans.append(matrix[x][y+1])
                    f[x][y+1] = 1
                    y = y + 1
                    t = 1
        return(ans)
#Runtime: 16 ms, faster than 72.15% of Python online submissions for Spiral Matrix.
#Memory Usage: 11.7 MB, less than 63.64% of Python online submissions for Spiral Matrix.