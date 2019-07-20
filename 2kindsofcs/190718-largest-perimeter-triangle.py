class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        length = len(A)
        a, b, c = length-3, length-2, length-1
        while a >= 0:
            if A[a] + A[b] > A[c]:
                return sum(A[a:a+3])
            a, b, c = a-1, b-1, c-1
        return 0
        
# Runtime: 68 ms, faster than 80.61% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 14.2 MB, less than 5.29% of Python3 online submissions for Largest Perimeter Triangle.
