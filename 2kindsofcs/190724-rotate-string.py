class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if A == B:
            return True
        AList = [ letter for letter in A ]
        BList = [ letter for letter in B ]
        ALength = len(A)
        BLength = len(B)
        if ALength != BLength:
            return False 
        for i in range(ALength):
            AList.append(AList.pop(0))
            if AList == BList:
                return True
        return False 
        
# Runtime: 32 ms, faster than 91.27% of Python3 online submissions for Rotate String.
# Memory Usage: 13.6 MB, less than 5.42% of Python3 online submissions for Rotate String.
