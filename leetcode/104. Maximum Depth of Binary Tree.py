from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    def dfs(r: Optional[TreeNode]) -> int:
      if r is None:
        return 0
      return 1 + max(dfs(r.left), dfs(r.right))
    return dfs(root)