"""
LeetCode : 821. Shortest Distance to a Character
problem : https://leetcode.com/problems/di-string-match/
"""

class Solution:
    def shortestToChar(self, S: str, C: str):

        result = []
        c_pos_list = [] # list that C's index in S
        c_pos_idx = 0  # C's index that will be compared with current s

        # Check All C's index in S
        for i, s in enumerate(S):
            if s == C:
                c_pos_list.append(i)


        # find shortest distance from the char c in the S
        for idx, s in enumerate(S):

            # case 1. s is C
            if s == C:
                result.append(0)
                c_pos_idx += 1
                continue

            # case 2. C is not yet desplayed
            if c_pos_idx == 0:
                # Calculate absolute value
                result.append(abs(idx - c_pos_list[c_pos_idx]))
                continue

            # Case 3. if new C, compare distance between previous C's index and current C's index
            if c_pos_idx < len(c_pos_list):
                result.append(min(abs(idx - c_pos_list[c_pos_idx -1]), abs(idx - c_pos_list[c_pos_idx])))
            else:
                # No new C exists
                result.append(abs(idx - c_pos_list[c_pos_idx -1]))
        return result

