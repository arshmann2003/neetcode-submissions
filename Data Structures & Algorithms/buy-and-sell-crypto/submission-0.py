class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, buyPrice in enumerate(prices):
            for j in range(i+1, len(prices)):
                sellPrice = prices[j]
                if (sellPrice - buyPrice) > maxProfit:
                    maxProfit = sellPrice - buyPrice
        return maxProfit
