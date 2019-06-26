"""
LeetCode : 824. Goat Latin
problem : https://leetcode.com/problems/goat-latin/
"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        list_s = S.split(' ')
        count = 1
        for idx, word in enumerate(list_s):
            if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                list_s[idx] += 'ma'
            else:
                list_s[idx] = (list_s[idx][1:] + list_s[idx][:1] + 'ma')
            list_s[idx] += 'a'*count
            count += 1
        return ' '.join(list_s)
