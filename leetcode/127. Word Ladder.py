from typing import List
from collections import deque

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    words = set(wordList)
    if endWord not in words:
      return 0
    queue = deque([(beginWord, 1)])
    while queue:
      w, steps = queue.popleft()
      if w == endWord:
        return steps
      for i in range(len(w)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
          nxt = w[:i] + c + w[i+1:]
          if nxt in words:
            words.remove(nxt)   # doubles as visited
            queue.append((nxt, steps + 1))
    return 0
