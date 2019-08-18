class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
        
        
# Runtime: 172 ms, faster than 5.14% of Python3 online submissions for Ransom Note.
# Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Ransom Note.

# 상대적으로 속도도 느리고 메모리도 많이 썼다. 어떻게 개선할까?
