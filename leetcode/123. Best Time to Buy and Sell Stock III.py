from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    hold = [float('-inf')] * 3
    cash = [0] * 3

    for p in prices:
      for i in range(1, 3):
        hold[i] = max(hold[i], cash[i - 1] - p)
        cash[i] = max(cash[i], hold[i] + p)
    return cash[2]
  
# test case: [1,2,1,4]

"""
hold[1] = -1
cash[1] = 0
hold[2] = -1
cash[2] = 0

hold1 = -1
cash1 = 1
hold2 = -1
cash2 = 1

hold1 = -1
cash1 = 1
hold2 = 0
cash2 = 1

hold1 = -1
cash1 = 3
hold2 = 0
cash2 = 4
"""