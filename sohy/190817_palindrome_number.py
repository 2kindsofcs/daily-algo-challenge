class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        idx1 = 0
        str_x = str(x)
        idx2 = len(str_x) - 1
        while (idx1 < idx2):
            if str_x[idx1] == str_x[idx2]:
                idx1 += 1 
                idx2 -= 1
            else:
                return False
        return True
        
        
        '''
        Runtime: 40 ms, faster than 91.29% of Python online submissions for Palindrome Number.
        Memory Usage: 11.8 MB, less than 40.96% of Python online submissions for Palindrome Number.
        '''