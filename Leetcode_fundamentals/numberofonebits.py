class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n : 
            n &= (n-1)
            res = res + 1 
        return res