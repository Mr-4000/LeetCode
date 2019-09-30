class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        digits[index] = digits[index] + 1
        while(digits[index]==10):
            digits[index] = 0
            index = index - 1
            if (index<0):
                digits.insert(0,0)
                index = 0
            digits[index] = digits[index] + 1
        return digits
#Runtime: 32 ms, faster than 96.92% of Python3 online submissions for Plus One.
#Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Plus One.