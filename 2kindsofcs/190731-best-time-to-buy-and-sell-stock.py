class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        minNum = max(prices)
        maxProfit = 0
        for price in prices:
            if price < minNum:
                minNum = price
            elif price - minNum > maxProfit:
                maxProfit = price - minNum
        return maxProfit
    
# Runtime: 72 ms, faster than 78.78% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.7 MB, less than 5.06% of Python3 online submissions for Best Time to Buy and Sell Stock.
