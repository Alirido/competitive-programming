from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def bt(i: List[int], p: List[int]) -> Optional[TreeNode]:
      if not i:
        return None
      root = TreeNode(p[-1])
      idx = i.index(p[-1])
      left = i[:idx]
      root.left = bt(left, p[:len(left)])
      right = i[idx + 1:]
      root.right = bt(right, p[len(left):-1])
      return root

    return bt(inorder, postorder)
  