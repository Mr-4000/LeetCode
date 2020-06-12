class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        C = copy.deepcopy(A)
        C.sort()
        for i in range(0,len(A)):
            min = 0
            max = len(C) - 1
            if (B[i] >= C[max]):
                A[i] = C[0]
                del C[0]
                continue
            while (min < max):
                mid = (min + max) / 2
                if (C[mid]>B[i]):
                    max = mid
                else:
                    min = mid + 1
            A[i] = C[mid]
            del C[mid]
            print(C)
        return A
#Runtime: 560 ms, faster than 13.78% of Python online submissions for Advantage Shuffle.
#Memory Usage: 15.2 MB, less than 25.00% of Python online submissions for Advantage Shuffle