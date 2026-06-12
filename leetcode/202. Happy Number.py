class Solution:
  def isHappy(self, n: int) -> bool:
    def calculate(x: int) -> int:
      result = 0
      while x > 0:
        digit = x % 10
        result += digit * digit
        x //= 10
      return result

    visited = set()
    while n not in visited and n != 1:
      visited.add(n)
      n = calculate(n)

    return n == 1
