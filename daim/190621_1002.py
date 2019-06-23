"""
LeetCode : 1002. Find Common Characters
problem : https://leetcode.com/problems/find-common-characters/
"""

class Solution:

    def commonChars(self, A):
        char_count_dict = {}
        result = []
        # init
        for character in A[0]:
            for ch in character:
                if ch in char_count_dict:
                    char_count_dict[ch] += 1
                    continue
                char_count_dict[ch] = 1
        # check other character
        for character in A[1:]:
            keys = list(char_count_dict.keys())
            for key in keys:
                # check existing spelling(key)
                count = character.count(key)
                if count:
                    if key in char_count_dict:
                        if char_count_dict[key] > count:
                            char_count_dict[key] = count
                else:
                    del char_count_dict[key]
        # make result
        for key in char_count_dict.keys():
            result.extend([key] * char_count_dict[key])
        return result
