class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        minPriceSoFar = float('inf')
        
        for curPrice in prices: 
            minPriceSoFar = min(curPrice, minPriceSoFar)
            profit = curPrice - minPriceSoFar
            maxProfit = max(maxProfit, profit)
            
        return maxProfit
        

        
'''
Runtime: 52 ms, faster than 38.01% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 12.6 MB, less than 35.78% of Python online submissions for Best Time to Buy and Sell Stock.

- redo [ ]
hard to understand the logic 

'''