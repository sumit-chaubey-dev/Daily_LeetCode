class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_profit = 0

        for price in prices:
            min_p = min(min_p, price)
            max_profit = max(max_profit, price - min_p)

        return max_profit