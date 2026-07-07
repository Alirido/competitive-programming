from typing import List
from collections import deque

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Node:
  def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
    self.val = val
    self.isLeaf = isLeaf
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomLeft = bottomLeft
    self.bottomRight = bottomRight

class Solution:
  def construct(self, grid: List[List[int]]) -> 'Node':
    n = len(grid)
    if n == 1:
      return Node(grid[0][0], True, None, None, None, None)

    def dfs(x1, y1, x2, y2):
      if x1 == x2 and y1 == y2:
        return Node(grid[x1][y1], True, None, None, None, None)

      midX = x1 + (x2 - x1) // 2
      midY = y1 + (y2 - y1) // 2

      topLeft = dfs(x1, y1, midX, midY)
      topRight = dfs(x1, midY + 1, midX, y2)
      bottomLeft = dfs(midX + 1, y1, x2, midY)
      bottomRight = dfs(midX + 1, midY + 1, x2, y2)

      leaf = (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
              and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val)
      if leaf:
        return Node(topLeft.val, True, None, None, None, None)
      return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

      
    return dfs(0, 0, n - 1, n - 1)

# TEST CASE
# Input: grid = [[0,1],[1,0]]