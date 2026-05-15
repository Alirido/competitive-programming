class Solution(object):
  def maxProfit(self, prices):
    max_profit = 0
    buy = 0

    for sell in range(1, len(prices)):
      current_profit = prices[sell] - prices[buy]
      if current_profit > max_profit:
        max_profit = current_profit
      elif current_profit < 0:
        buy = sell

    return max_profit