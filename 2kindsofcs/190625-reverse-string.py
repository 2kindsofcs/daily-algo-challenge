class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        lengthToCenter = length // 2
        index = 0
        while index < lengthToCenter:
            backIndex = -(index+1)
            if s[index] != s[backIndex]:
                s[index], s[backIndex] = s[backIndex], s[index]
            index += 1
        
    
# Runtime: 176 ms, faster than 44.42% of Python3 online submissions for Reverse String.
# Memory Usage: 17.7 MB, less than 41.98% of Python3 online submissions for Reverse String.
# 무난하게 성공. 더 빠른 방법이 있을 것 같다.
