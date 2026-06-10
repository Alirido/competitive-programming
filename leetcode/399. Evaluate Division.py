from typing import List
from collections import defaultdict

class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = defaultdict(dict)
    for i in range(len(equations)):
      graph[equations[i][0]][equations[i][1]] = values[i]
      graph[equations[i][1]][equations[i][0]] = 1 / values[i]

    def dfs(a: str, b: str) -> float:
      if b in graph[a]:
        return graph[a][b]
      visited.add(a)
      for x in graph[a]:
        if x in visited:
          continue
        val = dfs(x, b)
        if val != -1.0:
          return graph[a][x] * val
      return -1.0

    result = []
    for q in queries:
      a, b = q[0], q[1]
      if a not in graph or b not in graph:
        result.append(-1.0)
      elif a == b:
        result.append(1.0)
      else:
        visited = set()
        result.append(dfs(a, b))
    return result
