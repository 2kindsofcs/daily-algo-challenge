class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            return n / 5 + self.trailingZeroes(n / 5)
        
    '''
    - redo [ ]
    - idea: rather than generating factorial and dividing by 10 each time 
            keep finding factor of 5 (there are plenty of factors of 2 in factorial)
    
    '''
