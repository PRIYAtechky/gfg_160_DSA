from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        res = 0
        # Loop through prices starting from the second element
        for i in range(1, len(prices)):
            # If the current price is greater than the previous one, we add the difference to the result
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res