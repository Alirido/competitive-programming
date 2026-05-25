class Solution:
  def calculate(self, s: str) -> int:
    def helper(i: int) -> tuple[int, int]:
      result = 0
      sign = 1
      num = 0
      n = len(s)
      while i < n:
        c = s[i]
        if c.isdigit():
          num = num * 10 + int(c)
          i += 1
        elif c == '+':
          result += sign * num
          num = 0
          sign = 1
          i += 1
        elif c == '-':
          result += sign * num
          num = 0
          sign = -1
          i += 1
        elif c == '(':
          num, i = helper(i + 1)        # paren value becomes num
        elif c == ')':
          result += sign * num
          return result, i + 1
        else:                            # space
          i += 1
      return result + sign * num, i

    return helper(0)[0]
