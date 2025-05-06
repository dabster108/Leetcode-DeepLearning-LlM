class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        result = 0
        for ch in s:
            if ch != ' ':
                count += 1
                result = count
            else:
                count = 0
        return result
