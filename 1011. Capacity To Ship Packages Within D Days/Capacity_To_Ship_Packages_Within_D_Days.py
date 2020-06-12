class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        
        def pd(weights,D,n):
            t = 1
            s = 0
            for i in range(0,len(weights)):
                if (i==len(weights)-1):
                    continue
                s = s + weights[i]
                if ((s+weights[i+1])>n):
                    t = t + 1
                    s = 0
            if (t<=D):
                return 1
            else:
                return 0
        
        min = 0
        max = 0
        for i in weights:
            if (min<i):
                min = i
            max = max + i
        while (min<max):
            mid = (min + max) / 2
            if (pd(weights,D,mid)):
                max = mid
            else:
                min = mid + 1
        mid = (min + max) / 2
        return mid
#Runtime: 828 ms, faster than 8.68% of Python online submissions for Capacity To Ship Packages Within D Days.
#Memory Usage: 14.2 MB, less than 66.67% of Python online submissions for Capacity To Ship Packages Within D Days.