# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if node is None:
      return node

    visited = {}
    def dfs(nd: Node) -> Optional['Node']:
      if nd.val in visited:
        return visited[nd.val]
      visited[nd.val] = Node(nd.val)
      nb = []
      for v in nd.neighbors:
        nb.append(dfs(v))
      visited[nd.val].neighbors = nb
      return visited[nd.val]

    return dfs(node)
