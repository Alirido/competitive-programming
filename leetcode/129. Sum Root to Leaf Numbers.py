# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from typing import Optional
class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    total = 0
    def dfs(n: Optional[TreeNode], cur: str):
      nonlocal total
      cur = f"{cur}{n.val}"
      if n.left is None and n.right is None:
        total += int(cur)
        return
      if n.left:
        dfs(n.left, cur)
      if n.right:
        dfs(n.right, cur)
    dfs(root, "")
    return total