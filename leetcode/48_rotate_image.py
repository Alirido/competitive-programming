from typing import List

# Formula: [i, j] --> [j, n - i - 1]
# E.g. for 3x3 image: [0, 0] --> [0, 2]
# Sample 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Sample 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    n = layer = len(matrix)
    i = 0
    temp = None
    while layer > 1:
      a = i
      for j in range(layer - 1):
        b = i + j
        temp = matrix[a][b]
        x = temp
        for _ in range(4):
          temp = matrix[b][n - a - 1]
          matrix[b][n - a - 1] = x
          x = temp
          t = a
          a = b
          b = n - t - 1
      i += 1
      layer -= 2

class Solution: # improved version
  def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Step 1: transpose (swap matrix[i][j] with matrix[j][i] for i < j)
    for i in range(n):
      for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row
    for row in matrix:
      row.reverse()
