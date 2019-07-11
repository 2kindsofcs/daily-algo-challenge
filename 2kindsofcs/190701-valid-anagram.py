class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDic = {}
        if set(s) != set(t):
            return False
        for letter in s:
            if letter in letterDic:
                letterDic[letter] += 1
            else:
                letterDic[letter] = 1
        for letter in letterDic:
            if letter not in letterDic or letterDic[letter] != t.count(letter):
                return False
        return True
    
# Runtime: 48 ms, faster than 82.57% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13.3 MB, less than 68.83% of Python3 online submissions for Valid Anagram.
# 일단 허겁지겁 풀었는데, 좀 더 깔끔하게 풀 수는 없을까? 
