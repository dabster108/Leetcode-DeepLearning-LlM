class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        new_str = ""
        for i in range(len(x)):
            new_str += x[i]
        if new_str == new_str[::-1]:
            return True
        else:
            return False
