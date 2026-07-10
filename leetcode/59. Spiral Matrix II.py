from typing import List

class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    m = [[0] * n for _ in range(n)]
    top = left = 0
    bottom = right = n - 1
    num = 1
    for i in range(1, n + n):
      if i % 4 == 1: # left -> right
        for j in range(left, right + 1):
          m[top][j] = num
          num += 1
        top += 1
      elif i % 4 == 2: # top -> bottom
        for j in range(top, bottom + 1):
          m[j][right] = num
          num += 1
        right -= 1
      elif i % 4 == 3: # right -> left
        for j in range(right, left - 1, -1):
          m[bottom][j] = num
          num += 1
        bottom -= 1
      else: # bottom -> top
        for j in range(bottom, top - 1, -1):
          m[j][left] = num
          num += 1
        left += 1
    return m

if __name__ == "__main__":
  sol = Solution()
  print(sol.generateMatrix(3))
