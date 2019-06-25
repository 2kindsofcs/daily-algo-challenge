class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        currPointer = 0
        endPointer = len(A) - 1
        while currPointer < endPointer:
            if A[currPointer] % 2 != 0:
                if A[endPointer] % 2 == 0:
                    A[currPointer], A[endPointer] = A[endPointer], A[currPointer]
                endPointer -= 1
            else:
                currPointer += 1
        return A
    

# Runtime: 64 ms, faster than 92.10% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 13.7 MB, less than 62.65% of Python3 online submissions for Sort Array By Parity.
# 딱히 조건에 제약은 없었지만 다른 리스트 만들지 않고 주어진 리스트로만 해결하고 싶어서 포인터 두 개 만들어서 풀어보았다. 
