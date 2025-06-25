class Solution:
    def generateTag(self, caption: str) -> str:
        import re
        words = caption.split()
        cleaned_words = []
        for i, word in enumerate(words):
            cleaned = re.sub(r'[^a-zA-Z]', '', word)
            if cleaned:
                if i == 0:
                    cleaned_words.append(cleaned.lower())
                else:
                    cleaned_words.append(cleaned.capitalize())
        tag = '#' + ''.join(cleaned_words)
        return tag[:100]
