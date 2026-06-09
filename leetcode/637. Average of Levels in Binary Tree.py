from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    record = {}
    queue = deque([(root, 0)])
    while queue:
      r, level = queue.popleft()
      if level in record:
        record[level] = [record[level][0] + r.val, record[level][1] + 1]
      else:
        record[level] = [r.val, 1]
      if r.left is not None:
        queue.append((r.left, level + 1))
      if r.right is not None:
        queue.append((r.right, level + 1))
    result = [0] * len(record)
    for key, value in record.items():
      result[key] = value[0] / value[1]
    return result

