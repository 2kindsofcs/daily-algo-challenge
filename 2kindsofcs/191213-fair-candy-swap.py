class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        ALength = len(A)
        BLength = len(B)
        Asum = sum(A)
        Bsum = sum(B)
        halfDiff = (Asum - Bsum) / 2
        for i in range(BLength):
            target = halfDiff + B[i]
            if target in A:
                return [int(target), B[i]]
 
        
 # O(n)으로 줄였지만 여전히 Time limit exceeded
