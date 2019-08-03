class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        return False
    
# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.7 MB, less than 5.44% of Python3 online submissions for Detect Capital.
