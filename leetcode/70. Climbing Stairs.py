class Solution:
  def climbStairs(self, n: int) -> int: # using fibonacci
    solution = [0, 1, 2, 3]
    if n < 4:
      return solution[n]
    for i in range(4, n + 1):
      solution.append(solution[i - 1] + solution[i - 2])
    return solution[n]