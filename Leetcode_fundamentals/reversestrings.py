class Solution:
    def reverseString(self, s: List[str]) -> None:
        list_new = []
        for i in range(len(s) - 1, -1, -1):
            list_new.append(s[i])
        for i in range(len(s)):
            s[i] = list_new[i]
