"""
LeetCode : 461. Hamming Distance
problem : https://leetcode.com/problems/hamming-distance/
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_bit = bin(x ^ y)
        result = xor_bit[2:]
        return result.count('1')
