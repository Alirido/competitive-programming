from typing import Optional
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    def process(currRoot: Optional[TreeNode]) -> TreeNode:
      if currRoot is None or (currRoot.left is None and currRoot.right is None):
        return currRoot
      elif currRoot.right is None:
        currLeaf = process(currRoot.left)
        currRoot.right = currRoot.left
        currRoot.left = None

        return currLeaf
      elif currRoot.left is None:
        return process(currRoot.right)
      else:
        leftLeaf = process(currRoot.left)
        rightLeaf = process(currRoot.right)
        leftLeaf.right = currRoot.right
        currRoot.right = currRoot.left
        currRoot.left = None

        return rightLeaf

    process(root)
        