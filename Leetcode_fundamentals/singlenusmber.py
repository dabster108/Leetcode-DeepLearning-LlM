from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        list_output = []
        for i in nums:
            if nums.count(i) == 1:
                list_output.append(i)
        return list_output
