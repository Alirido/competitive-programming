class Solution(object):
  def spiralOrder(self, matrix):
    i = j = 0
    visited = set()
    result = []
    direction = "right"
    m = len(matrix)
    n = len(matrix[i])

    if m == n == 1:
      return [matrix[i][j]]

    while True:
      if (i, j) in visited:
        break
      else:
        match direction:
          case "right":
            while j < n and (i, j) not in visited:
              visited.add((i, j))
              result.append(matrix[i][j])
              j += 1
            direction = "down"
            j -= 1
            i += 1
          case "down":
            while i < m and (i, j) not in visited:
              visited.add((i, j))
              result.append(matrix[i][j])
              i += 1
            direction = "left"
            i -= 1
            j -= 1
          case "left":
            while j >= 0 and (i, j) not in visited:
              visited.add((i, j))
              result.append(matrix[i][j])
              j -= 1
            direction = "up"
            j += 1
            i -= 1
          case "up":
            while i >= 0 and (i, j) not in visited:
              visited.add((i, j))
              result.append(matrix[i][j])
              i -= 1
            direction = "right"
            i += 1
            j += 1
    return result
  
  def spiralOrder(self, matrix): # The boundary approach
    if not matrix or not matrix[0]:
      return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
      for j in range(left, right + 1):
        result.append(matrix[top][j])
      top += 1

      for i in range(top, bottom + 1):
        result.append(matrix[i][right])
      right -= 1

      if top <= bottom:
        for j in range(right, left - 1, -1):
          result.append(matrix[bottom][j])
        bottom -= 1

      if left <= right:
        for i in range(bottom, top - 1, -1):
          result.append(matrix[i][left])
        left += 1

    return result
