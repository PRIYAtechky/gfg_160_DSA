class Solution:
    def maximumProfit(self, prices):

        if not prices or len(prices) < 2:
            return 0
        
        minSoFar = prices[0]
        res = 0
        
        for i in range(1, len(prices)):
            minSoFar = min(minSoFar, prices[i])
            res = max(res, prices[i] - minSoFar)
        
        return res