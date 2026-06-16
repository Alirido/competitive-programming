from typing import List
from collections import deque

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]
    prereq = [0] * numCourses

    for a, b in prerequisites:
      graph[b].append(a)
      prereq[a] += 1

    queue = deque([i for i in range(numCourses) if prereq[i] == 0])
    order = []

    while queue:
      course = queue.popleft()
      order.append(course)
      for child in graph[course]:
        prereq[child] -= 1
        if prereq[child] == 0:
          queue.append(child)

    return order if len(order) == numCourses else []
