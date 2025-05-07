from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ""
        for i in range(len(digits)):
            digit = digit + str(digits[i])
        result = int(digit)
        result = result + 1
        lst = []
        for ch in str(result):  
            lst.append(int(ch)) 
        return lst
