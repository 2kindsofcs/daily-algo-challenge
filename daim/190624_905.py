"""
LeetCode : 905. Sort Array By Parity
problem : https://leetcode.com/problems/sort-array-by-parity/
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        even.extend(odd)
        return even