class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)
        Dnum, Inum = N , 0
        result = []
        for i in range(0, N):
            if S[i] == "D":
                result.append(Dnum)
                Dnum = Dnum - 1
            else:
                result.append(Inum)
                Inum += 1
        if S[-1] == "D":
            result.append(Dnum)
        else:
            result.append(Inum)
        return result
            
# Runtime: 108 ms, faster than 25.91% of Python3 online submissions for DI String Match.
# Memory Usage: 14.3 MB, less than 55.42% of Python3 online submissions for DI String Match.
