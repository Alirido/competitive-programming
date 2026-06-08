from typing import List
from collections import deque

class Solution:
  def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
    if startGene == endGene:
      return 0
    bank = set(bank)
    queue = deque([(startGene, 0)])
    visited = set()
    while queue:
      cur, steps = queue.popleft()
      if cur == endGene:
        return steps
      
      for i in range(8):
        for x in "ACGT":
          if x == cur[i]:
            continue
          nxt = cur[:i] + x + cur[i + 1:]
          if nxt in bank and nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, steps + 1))
      
    return -1
