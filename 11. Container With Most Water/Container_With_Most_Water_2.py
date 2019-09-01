#还是使用2 pointer approach,两头逼近，把较低的一个往里进一步
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        i =0
        j = len(height) - 1
        while (i<j):
            if (height[i]<height[j]):
                h = height[i]
            else:
                h = height[j]
            area = h * (j-i)
            if (area > max):
                max = area
            if (height[i]<height[j]):
                i = i + 1
            else:
                j = j - 1
        return max
#Runtime: 96 ms, faster than 94.03% of Python online submissions for Container With Most Water.
#Memory Usage: 13 MB, less than 84.75% of Python online submissions for Container With Most Water.
