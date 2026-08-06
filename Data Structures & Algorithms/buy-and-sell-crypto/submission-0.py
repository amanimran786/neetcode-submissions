class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for price in prices:
            if price < lowest:
                lowest = price

            current_profit = price - lowest

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit        