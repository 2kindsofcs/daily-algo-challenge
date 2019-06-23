"""
LeetCode : 1078. Occurrences After Bigram
problem : https://leetcode.com/problems/occurrences-after-bigram/
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split()
        last_index = len(text_list) - 1
        result = []
        for idx, txt in enumerate(text_list):
            if txt == second:
                if 0 <= idx - 1 and idx + 1 <= last_index:
                    if text_list[idx - 1] == first:
                        result.append(text_list[idx + 1])
        return result
