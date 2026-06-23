from collections import deque

class Solution:
  def isValid(self, s: str) -> bool:
    left = None
    for c in s:
      match c:
        case "(" | "{" | "[":
          if left is None:
            left = deque([c])
          else:
            left.append(c)
        case _:
          if not left:
            return False
          else:
            x = left.pop()
            match x:
              case "(":
                if c != ")":
                  return False
              case "[":
                if c != "]":
                  return False
              case "{":
                if c != "}":
                  return False
    return True if not left else False