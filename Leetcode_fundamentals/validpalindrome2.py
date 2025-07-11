class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                # Try skipping character at i or at n - 1 - i
                return is_palindrome(s[i+1:n-i]) or is_palindrome(s[i:n-1-i])
        return True
