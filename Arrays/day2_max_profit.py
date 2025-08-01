class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # Initialize with a very high number
        max_profit = 0  # No profit yet

        for price in prices:
            # If we find a new minimum price, update min_price
            if price < min_price:
                min_price = price
            # Else calculate profit if we sell at this price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit