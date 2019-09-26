class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        ans = []
        for i in intervals:
            if (ans==[]):
                ans.append(i)
            if (i[0] > ans[-1][1]):
                ans.append(i)
            else:
                if (i[1] > ans[-1][1]):
                    ans[-1][1] = i[1]
        return ans
#Runtime: 96 ms, faster than 91.64% of Python3 online submissions for Merge Intervals.
#Memory Usage: 15.8 MB, less than 6.52% of Python3 online submissions for Merge Intervals.