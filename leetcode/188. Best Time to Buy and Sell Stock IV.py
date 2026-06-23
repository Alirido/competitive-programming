from typing import List

class Solution:
  def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    if n == 0 or k == 0:
      return 0

    # Big-k shortcut: with k >= n // 2 the limit no longer binds, so this
    # reduces to "buy/sell as often as you like" -> sum every up-day delta.
    # (This is essentially the simpler problem you already solved.)
    if k >= n // 2:
      return sum(
        max(0, prices[i] - prices[i - 1])
        for i in range(1, n)
      )

    # hold[t] = best profit while currently holding, this buy counts as txn t
    # cash[t] = best profit after completing t full transactions
    hold = [float('-inf')] * (k + 1)
    cash = [0] * (k + 1)

    for p in prices:
      for t in range(1, k + 1):
        # buy now -> open txn t, starting from cash after t-1 txns
        hold[t] = max(hold[t], cash[t - 1] - p)
        # sell now -> close txn t
        cash[t] = max(cash[t], hold[t] + p)

    return cash[k]
