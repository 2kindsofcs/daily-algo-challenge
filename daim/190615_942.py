"""
LeetCode : 942. DI String Match
problem : https://leetcode.com/problems/di-string-match/
"""

class Solution:
    def diStringMatch(self, S: str) :
        min = -1
        max = len(S) + 1
        A = []
        for idx, s in enumerate(S):
            if S[idx] == "I":
                min += 1
                A.append(min)

            if S[idx] == 'D':
                max -= 1
                A.append(max)
        A.append(min + 1)
        return A