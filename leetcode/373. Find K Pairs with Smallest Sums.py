import heapq
from typing import List

# My note: use heap to utilize priority queue, which will always pop the smallest in the nodes.
class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    if not nums1 or not nums2:
      return []

    heap = [] 
    # Seed with the first column: pair each nums1[i] with nums2[0].
    # Only need min(k, len(nums1)) rows — we'll never use more than k.
    for i in range(min(k, len(nums1))):
      heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    result = []
    while heap and len(result) < k:
      _, i, j = heapq.heappop(heap)
      result.append([nums1[i], nums2[j]])
      # Advance within this row: the next candidate is (i, j+1)
      if j + 1 < len(nums2):
        heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result
