class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        ALength = len(A)
        BLength = len(B)
        Asum = sum(A)
        Bsum = sum(B)
        diff = Asum - Bsum
        checked = {}
        for i in range(ALength):
            if A[i] not in checked:
                checked[A[i]] = []
            for j in range(BLength):
                if B[j] in checked[A[i]]:
                    continue
                if diff == ((2 * A[i]) - (2 * B[j])):
                    return [A[i], B[j]]
                else:
                    checked[A[i]].append(B[j])  
        
 # Time limit exceeded
