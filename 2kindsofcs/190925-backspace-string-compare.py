class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        indexS, indexT = len(S) - 1, len(T) - 1
        stackS, stackT = [], []
        count = 0
        while indexS >= 0:
            if S[indexS] == "#":
                count += 1 
            else:
                if count:
                    indexS -= 1
                    count -= 1
                    continue
                if not count:
                    stackS.append(S[indexS])
            indexS -= 1
        count = 0 
        while indexT >= 0:
            if T[indexT] == "#":
                count += 1 
            else:
                if count:
                    indexT -= 1
                    count -= 1
                    continue
                if not count:
                    stackT.append(T[indexT])
            indexT -= 1
        return stackS == stackT
                    
# Runtime: 44 ms, faster than 9.20% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 14 MB, less than 8.00% of Python3 online submissions for Backspace String Compare.
# 처음 짰던 코드가 속도도 메모리도 영 결과가 좋지 못해서 다른 방법으로도 풀었는데, 코드가 가독성도 떨어지고 별로인 것 같다.
# 속도를 향상시키려면 어떤 방식으로 접근해야 하는 걸까?
