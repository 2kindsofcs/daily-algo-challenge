class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hexdict = {10:'a', 11:'b', 12:'c', 13: 'd', 14: 'e', 15:'f'}
        retStr = ""
        
        if num == 0:
            return str(0)
        elif num < 0:
            num &= 0xFFFFFFFF
        
        while num > 0:
            remainder = num % 16 
            if remainder < 10:
                retStr += str(remainder)
            else:
                retStr += hexdict[remainder] 
            num /= 16 
            
        return retStr[::-1]