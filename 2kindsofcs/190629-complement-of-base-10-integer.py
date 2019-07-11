class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binNum = bin(N)
        compleList = []
        result = 0
        for bit in binNum[2:]:
            if bit == '0':
                compleList.append('1')
            else:
                compleList.append('0')
        compleList.reverse()
        for index, bit in enumerate(compleList):
            if bit == '1':
                result += 2 ** index
        return result
    
# Runtime: 28 ms, faster than 97.78% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 13.2 MB, less than 31.50% of Python3 online submissions for Complement of Base 10 Integer.
