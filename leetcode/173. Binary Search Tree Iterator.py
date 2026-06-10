from typing import Optional
import heapq
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class BSTIterator:
  def __init__(self, root: Optional[TreeNode]):
    self.heap = []
    queue = deque([root])
    while queue:
      r = queue.popleft()
      if r is None:
        continue
      heapq.heappush(self.heap, r.val)
      queue.append(r.left)
      queue.append(r.right)
    self.length = len(self.heap)

  def next(self) -> int:
    return heapq.heappop(self.heap)

  def hasNext(self) -> bool:
    return len(self.heap) > 0
  

class BSTIterator: # Optimizer approach using in-order traversal
  def __init__(self, root):
      self.stack = []
      self._push_left(root)

  def _push_left(self, node):
      while node:
          self.stack.append(node)
          node = node.left

  def next(self) -> int:
      node = self.stack.pop()
      self._push_left(node.right)
      return node.val

  def hasNext(self) -> bool:
      return bool(self.stack)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()