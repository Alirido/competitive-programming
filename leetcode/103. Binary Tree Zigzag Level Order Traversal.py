from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []
    queue = deque([(root, 0)])
    bt_list = {}
    while queue:
      r, level = queue.popleft()
      if not r:
        continue
      if level in bt_list:
        bt_list[level].append(r.val)
      else:
        bt_list[level] = [r.val]
      queue.append((r.left, level + 1))
      queue.append((r.right, level + 1))
    
    result = []
    for k, v in bt_list.items():
      if k % 2 == 0:
        result.append(v)
      else:
        result.append(v[::-1])
    return result
  
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # Cleaner solution
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):  # snapshot current level size
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right
    return result