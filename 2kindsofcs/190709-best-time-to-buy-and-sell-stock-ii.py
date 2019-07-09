class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        profit = 0
        length = len(prices)
        for i in range(length-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit = profit + diff
        return profit

# Runtime: 40 ms, faster than 74.69% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 13.9 MB, less than 86.31% of Python3 online submissions for Best Time to Buy and Sell Stock II.

# 뭘 해야 할지는 알겠는데 구체적으로 코드를 어떻게 작성해야할지 조금 헤매다가, 금방 쉽게 풀었다. 
# 뭐가 중요하고 중요하지 않은지, 진짜 필요한 게 뭔지 지금보다 더 빠르게 파악해야 한다. 
