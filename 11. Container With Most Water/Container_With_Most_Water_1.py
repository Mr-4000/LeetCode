class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        max = 0
        for i in range(0,l-1):
            for j in range(i+1,l):
                if (height[i] < height[j]):
                    h = height[i]
                else:
                    h = height[j]
                ans = h * (j - i)
                if (ans > max):
                    max = ans
        return(max)
#O(N^2)的运行效率太低，导致出现超时错误