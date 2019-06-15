class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)
        Dnum, Inum = N , 0
        result = []
        # 순서대로 한 문자씩 가져와서 판별하면 되므로 꼭 range 사용하지 않아도 됨
        for letter in S:
            if letter == "D":
                result.append(Dnum)
                Dnum = Dnum - 1
            else: # letter == "I"
                result.append(Inum)
                Inum = Inum + 1
        # 판별하지 않고 바로 Inum을 뒤에 붙이고 끝냄
        result.append(Inum) # 사실 Inum == Dnum인데 편의상 그냥 Inum 씀 
        return result
            
# Runtime: 88 ms, faster than 91.10% of Python3 online submissions for DI String Match.
# Memory Usage: 14.2 MB, less than 67.40% of Python3 online submissions for DI String Match.
