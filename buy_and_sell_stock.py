class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 9999
        max_profit = 0

        # Iterate over each price in the prices array
        for price in prices:
            # If the current price is lower than the minimum price, update min_price
            if price < min_price:
                min_price = price
            else:
                # Otherwise, calculate the profit if sold at this price
                profit = price - min_price
                # Update max_profit if this is the highest profit so far
                if profit > max_profit:
                    max_profit = profit

        # Return the maximum profit found
        return max_profit


prices = [7, 1, 5, 3, 6, 4]

# Creating a solution instance
solution = Solution()

output = solution.maxProfit(prices)

# Output the result
print(output)