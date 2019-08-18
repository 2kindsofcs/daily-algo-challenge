class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        rList = []
        divisor = 10
        while True:
            remainder = x % divisor
            rList.append(remainder)
            divisor = divisor * 10
            if remainder == x:
                break
        length = len(rList)
        reversedNum = 0
        power = length - 1 
        for i in range(length):
            reversedNum += (rList[i] // (10 ** i)) * (10 ** power)
            power -= 1 
        return x == reversedNum
    
# Runtime: 128 ms, faster than 5.50% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.2 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
