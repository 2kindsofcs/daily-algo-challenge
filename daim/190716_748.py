"""
LeetCode : 748. Shortest Completing Word
problem : https://leetcode.com/problems/shortest-completing-word/
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        ch_count_list = {}

        # extract alpha and change uppercase to lowercase
        for s in licensePlate.lower():
            if s.isalpha():
                if ch_count_list.get(s):
                    ch_count_list[s] += 1
                else:
                    ch_count_list[s] = 1

        min_count_word = ''
        for word in words:
            for key in ch_count_list.keys():
                key_count = ch_count_list[key]
                if word.count(key) < key_count:
                    break
            else:
                #  change more shortest completing Word
                if min_count_word == '' or len(word) < len(min_count_word):
                    min_count_word = word
        return min_count_word
