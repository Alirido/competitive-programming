from typing import List

class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    chars = {
      "2": "abc",
      "3": "def",
      "4": "ghi",
      "5": "jkl",
      "6": "mno",
      "7": "pqrs",
      "8": "tuv",
      "9": "wxyz",
    }

    result = []
    n = len(digits)
    def backtracking(curr: str):
      x = len(curr)
      if x == n:
        result.append(curr)
        return
      for c in chars[digits[x]]:
        backtracking(curr + c)
    backtracking("")
    return result