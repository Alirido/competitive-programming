from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    result = -1001
    def dfs(r: Optional[TreeNode]) -> int:
      nonlocal result
      if r is None:
        return 0
      left = max(dfs(r.left), 0)
      right = max(dfs(r.right), 0)
      result = max(result, r.val + left + right)
      return r.val + max(left, right)

    dfs(root)
    return result
