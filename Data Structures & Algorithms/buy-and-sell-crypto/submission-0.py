class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, L = 0,0

        for R in range(len(prices)):
            if prices[R] - prices[L] > 0:
                profit = max(prices[R] - prices[L],profit)
            if prices[L] > prices[R]:
                L = R
        return profit
            
        