class Solution:
    def binaryGap(self, N: int) -> int:
        if N == 0:
            return 0
        binNum = bin(N)[3:]
        countList = []
        count = 0
        for bit in binNum:
            count = count + 1 
            if bit == "1":
                countList.append(count)
                count = 0 
        return max(countList) if countList else 0

# Runtime: 32 ms, faster than 89.55% of Python3 online submissions for Binary Gap.
# Memory Usage: 13.2 MB, less than 57.41% of Python3 online submissions for Binary Gap.

# 처음에 boolean 타입의 일종의 플래그를 세워서 체크해야하나? 하고 생각했다가 어떻게 처리해야 할지 잘 떠오르지 않아서 count를 썼다. 
# 약 15분 정도 걸린 듯 하다.
