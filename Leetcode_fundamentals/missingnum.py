from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n += 1  

        for j in range(n + 1): 
            found = False
            for i in range(n):
                if nums[i] == j:
                    found = True
                    break
            if not found:
                return j