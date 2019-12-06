class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        half = (length // 2) + 1
        for i in range(1, half):
            if s[:i] == s[i:(2 * i)]:
                quo = length // i
                if s[:i] * quo == s:
                    return True
        return False
                
# Runtime: 96 ms, faster than 42.38% of Python3 online submissions for Repeated Substring Pattern.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Repeated Substring Pattern.
