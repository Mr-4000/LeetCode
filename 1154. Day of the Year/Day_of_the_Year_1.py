class Solution:
    def dayOfYear(self, date: str) -> int:
        month = {1:31,2:28,3:31,4:30,5:31,6:30,
                7:31,8:31,9:30,10:31,11:30,12:31}
        l = date.split("-")
        y = int(l[0])
        m = int(l[1])
        d = int(l[2])
        import calendar
        if (calendar.isleap(y)):
            month[2] = 29
        t = 0
        for i in range(1,m):
            t = t + month[i]
        return (t + d)

#Runtime: 32 ms, faster than 92.10% of Python3 online submissions for Day of the Year.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Day of the Year.