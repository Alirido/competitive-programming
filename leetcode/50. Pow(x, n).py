from functools import lru_cache
class Solution:
  def myPow(self, x: float, n: int) -> float:
    @lru_cache
    def recursive(pow: int) -> float:
      if pow == 0:
        return 1
      elif pow == 1:
        return x
      elif pow == 2:
        return x * x
      reminder = pow % 2
      half = pow // 2
      return recursive(half) * recursive(half + reminder)
    return recursive(n) if n >= 0 else 1 / recursive(n * -1)