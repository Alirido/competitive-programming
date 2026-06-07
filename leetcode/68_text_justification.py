from typing import List
class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    result = []
    length = 0
    start = end = 0
    for i, w in enumerate(words):
      n = end - start
      if length == 0 or length + len(w) + n + 1 <= maxWidth:
        length += len(w)
        end = i
      else:
        spaces = maxWidth - length
        remainingSpaces = spaces % n if n > 0 else 0
        if n == 0:
          line = words[start] + " " * (maxWidth - len(words[start]))
        elif remainingSpaces == 0:
          line = (" " * (spaces // n)).join(words[start:end + 1])
        else:
          distributedSpaces = " " * (spaces // n)
          line = (distributedSpaces + " ").join(words[start:start + remainingSpaces + 1]) + distributedSpaces + distributedSpaces.join(words[start + remainingSpaces + 1:end + 1])
        result.append(line)
        start = end = i
        length = len(w)
    # left-justified
    line = " ".join(words[start:end + 1])
    line += " " * (maxWidth - len(line))
    result.append(line)

    return result
