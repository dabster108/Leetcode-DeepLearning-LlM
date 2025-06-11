import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        filtered_words = [word for word in words if word not in banned]
        word_counts = Counter(filtered_words)
        return word_counts.most_common(1)[0][0]
