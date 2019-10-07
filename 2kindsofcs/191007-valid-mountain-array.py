class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
        length = len(A)
        minimum = min(A)
        maximum = max(A)
        if minimum == maximum:
            return False
        if A[0] == maximum or A[-1] == maximum:
            return False
        if A.count(maximum) > 1:
            return False
        maxIndex = A.index(maximum)
        if len(set(A[0:maxIndex])) != len(A[0:maxIndex]):
            return False
        if len(set(A[maxIndex+1:])) != len(A[maxIndex+1:]):
            return False
        if A[0:maxIndex] == sorted(A[0:maxIndex]) and A[maxIndex+1:] == sorted(A[maxIndex+1:], reverse=True):
            return True
        return False

# Runtime: 252 ms, faster than 23.42% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.8 MB, less than 5.26% of Python3 online submissions for Valid Mountain Array.

