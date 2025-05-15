class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ''' 
        Excel column title conversion:
        28 - 1 = 27
        27 % 26 = 1 → B
        27 // 26 = 1
        1 - 1 = 0 → A
        Result = AB
        '''
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result
            columnNumber //= 26
        return result
