class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        frag = []
        f = []
        for i in range(0,n):
            for j in range(0,n):
                frag.append(0)
            ans.append(frag)
            f.append(frag)
            frag = []
        t = 1
        x=0
        y=0
        ans[0][0] = 1
        for i in range(2,n*n+1):
            if (t==1):
                if ((y+1<n)and(f[x][y+1]==0)):
                    f[x][y+1] = 1
                    ans[x][y+1] = i
                    y = y + 1
                else:
                    f[x+1][y] = 1
                    ans[x+1][y] = i
                    x = x + 1
                    t = 2
                    continue
            if (t==2):
                if ((x+1<n)and(f[x+1][y]==0)):
                    f[x+1][y] = 1
                    ans[x+1][y] = i
                    x = x + 1
                else:
                    f[x][y-1] = 1
                    ans[x][y-1] = i
                    y = y - 1
                    t = 3
                    continue
            if (t==3):
                if ((y-1>=0)and(f[x][y-1]==0)):
                    f[x][y-1] = 1
                    ans[x][y-1] = i
                    y = y - 1
                else:
                    f[x-1][y]=1
                    ans[x-1][y] = i
                    x = x - 1
                    t = 4
                    continue
            if (t==4):
                if ((x-1>=0)and(f[x-1][y]==0)):
                    f[x-1][y] = 1
                    ans[x-1][y] = i
                    x = x - 1
                else:
                    f[x][y+1] = 1
                    ans[x][y+1] = i
                    y = y + 1
                    t = 1
        return(ans)
#Runtime: 36 ms, faster than 85.98% of Python3 online submissions for Spiral Matrix II.
#Memory Usage: 13.5 MB, less than 9.09% of Python3 online submissions for Spiral Matrix II.