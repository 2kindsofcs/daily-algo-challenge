class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret_set = set()
        maxI = 0
        countI = 0
        maxJ = 0
        countJ = 0
        
        if x == 1:
            maxI = 1
        else:
            while True:
                if bound < x**countI:
                    maxI = countI
                    break 
                else: 
                    countI += 1
        if y == 1:
            maxJ = 1
        else:
            while True:
                if bound < y**countJ:
                    maxJ = countJ
                    break 
                else: 
                    countJ += 1
                
        for i in range(maxI):
            for j in range(maxJ):
                num = x**i + y**j
                if num <= bound:
                    ret_set.add(num)
                    
        return list(ret_set)
    
    
    '''
    Runtime: 8 ms, faster than 98.22% of Python online submissions for Powerful Integers.
    Memory Usage: 11.8 MB, less than 25.00% of Python online submissions for Powerful Integers.
    
    
    '''
        
        