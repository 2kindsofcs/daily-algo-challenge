class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s) 
        if length == 0 or s == t:
            return True
        for letter in s:
            if letter not in t:
                return False
        index = 0
        for letter in t:
            if letter == s[index]:
                index += 1
            if index == length:
                return True
        return False
        

# Runtime: 96 ms, faster than 80.14% of Python3 online submissions for Is Subsequence.
# Memory Usage: 18.4 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
# "" 같은 극단적인 입력값 처리를 깔끔하게 하고 싶다. 
