class Solution:
    def countDigitOne(self, n: int) -> int:
        last = 0
        d = 1
        total = 0
        low = 0
        new = 0
        while (n > 0):
            last = n % 10
            n = n // 10
            if (last == 0):
                new = n * d
            if (last == 1):
                new = n * d + low + 1
            if (last >=2):
                new = (n + 1) * d
            low = last * d + low
            d = d * 10
            total = total + new
        return total
#Runtime: 20 ms, faster than 98.31% of Python3 online submissions for Number of Digit One.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Digit One.