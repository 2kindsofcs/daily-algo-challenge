import string

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alphabets = string.ascii_lowercase
        alphabetNum = len(alphabets)
        s = s.lower()
        t = t.lower()
        letterList = [ 0 for _ in range (alphabetNum) ]
        for letter in s:
            index = alphabets.index(letter)
            letterList[index] += 1
        for letter in t:
            index = alphabets.index(letter)
            letterList[index] -= 1
            if letterList[index] < 0:
                return letter
        
        
# Runtime: 48 ms, faster than 22.59% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Find the Difference.
