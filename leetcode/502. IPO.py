import heapq
from typing import List

class Solution:
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    pairs = sorted(zip(capital, profits))
    heap = []
    i = 0
    for _ in range(k):
      while i < len(pairs) and pairs[i][0] <= w:
        heapq.heappush(heap, -pairs[i][1]) # using negative because we want it to be max-heap instead of the min-heap as the default of heapq
        i += 1
      if not heap:
        break
      w -= heapq.heappop(heap)
    return w
