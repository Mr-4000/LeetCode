#attention! Must use the set function or face a time problem
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        suma = sum(A)
        sumb = sum(B)
        setb = set(B)
        temp = suma - sumb
        for x in A:
            tar = x - temp // 2
            if (tar in setb):
                return [x,tar]
#Runtime: 412 ms, faster than 97.28% of Python3 online submissions for Fair Candy Swap.
#Memory Usage: 16.3 MB, less than 8.33% of Python3 online submissions for Fair Candy Swap.