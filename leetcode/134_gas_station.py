class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    total = 0
    sum_gas = 0
    starting_index = 0

    for i in range(len(gas)):
      diff = gas[i] - cost[i]
      total += diff
      sum_gas += diff
      if sum_gas < 0:
        starting_index = i + 1
        sum_gas = 0

    return starting_index if total >= 0 else -1
