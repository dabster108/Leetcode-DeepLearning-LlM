from collections import defaultdict
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        h1 = defaultdict(int)
        for i in range(n):
            h2 = h1
            h1 = defaultdict(int)
            for j in range(len(words[i])):
                h1[words[i][j]] += 1
            if i > 0:
                for c in h1:
                    h1[c] = min(h1[c], h2[c])
        for c in h1:
            while h1[c] > 0:
                res.append(c)
                h1[c] -= 1
        return res