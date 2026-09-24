class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0

        ## in the future : after the index
        ## look for the max profit, in either n2 or n : n is better
        ## double nested loop is easy but better way ??
        current_buy = prices[0]
        max_profit =0
        profit = 0
        for i in range(1, len(prices)):
            profit = max(0, prices[i] - current_buy )
            if profit == 0:
                current_buy = prices[i]
                print(current_buy)

            max_profit = max(profit, max_profit)
        return max_profit