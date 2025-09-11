class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        profit = 0

        for i in range(len(prices)): 

            cheapest = min(prices[i], cheapest)
            profit = max(profit, prices[i] - cheapest) 
            
        return profit