from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def build(po: List[int], io: List[int]) -> Optional[TreeNode]:
      if not po or not io:
        return None
      root = TreeNode(po[0])
      idx = io.index(po[0])
      root.left = build(po[1:idx + 1], io[:idx])
      root.right = build(po[idx + 1:], io[idx + 1:])
      return root

    return build(preorder, inorder)