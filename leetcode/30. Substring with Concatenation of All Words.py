from typing import List
from collections import Counter
import textwrap

class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    counter_check = Counter(words)
    s_check = set(["".join(words)])
    word_len = len(words[0])
    i = 0
    j = len(words) * word_len
    result = []
    while j <= len(s):
      if s[i:j] in s_check:
        result.append(i)
      else:
        counter = Counter(textwrap.wrap(s[i:j], word_len))
        if counter == counter_check:
          result.append(i)
          s_check.add(s[i:j])
      i += 1
      j += 1
    return result


if __name__ == "__main__":
  print(set("".join(["ali", "rido"])))