class Solution(object):
  def maxProfit(self, prices):
    total_profit = 0

    for i in range(len(prices) - 1):
      current_profit = prices[i + 1] - prices[i]
      if current_profit > 0:
        total_profit += current_profit

    return total_profit