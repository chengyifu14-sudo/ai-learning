class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price<min_price:
                min_price=price
            profit=price-min_price
            if profit>max_profit:
                max_profit=profit

            # 1. 如果 price 比 min_price 小，就更新 min_price
            # 2. 算今天卖的利润 price - min_price
            # 3. 如果利润比 max_profit 大，就更新 max_profit
        return max_profit