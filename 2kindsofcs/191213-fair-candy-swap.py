class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        Asum = sum(A)
        Bsum = sum(B)
        A = set(A)
        B = set(B)
        halfDiff = (Asum - Bsum) / 2
        for num in B:
            target = halfDiff + num
            if target in A:
                return [int(target), num]

# Runtime: 408 ms, faster than 80.23% of Python3 online submissions for Fair Candy Swap.
# Memory Usage: 15.6 MB, less than 8.33% of Python3 online submissions for Fair Candy Swap.
        
# 핵심은 크게 2가지였다. 최소한의 연산으로, 중복되는 요소 없이 확인하기.
