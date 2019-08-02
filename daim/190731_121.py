"""
LeetCode : 121. Best Time to Buy and Sell Stock
problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Solution :
heapq는 이진트리 기반의 최소힙 자료구조이며 첫번째 원소는 항상 최솟값이다.
heqpq에 prices의 값을 하나씩 push하게 되면 항상 작은 값이 맨 앞에 위치하게 되고
이 성질을 이용하면 현재까지의 최소 price와 현재의 price와의 차(diff)의 값을 구할 수 있게 된다.
"""
import heapq

class Solution(object):
    def maxProfit(self, prices):
        """
        Time    O(nlogn)
        Space   O(n) heap
        """
        if len(prices) < 2:
            return 0
        pq = []
        diff = 0
        for price in prices:
            heapq.heappush(pq, price)
            if price - pq[0] > diff:
                diff = price - pq[0]
        return diff

s = Solution()
s.maxProfit([7,1,5,3,6,4])
