from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []
    q = deque([root])
    result = []
    while q:
      n = len(q)
      value = []
      for _ in range(n):
        r = q.popleft()
        value.append(r.val)
        if r.left is not None:
          q.append(r.left)
        if r.right is not None:
          q.append(r.right)
      result.append(value)
    return result

