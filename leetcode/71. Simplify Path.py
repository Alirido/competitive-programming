from collections import deque

class Solution:
  def simplifyPath(self, path: str) -> str:
    queue = deque()
    dir = ""
    for c in path[1:]:
      if c == "/":
        match dir:
          case "..":
            if queue:
              queue.pop()
          case "." | "":
            pass
          case _:
            queue.append(dir)
        dir = ""
      else:
        dir += c
    match dir:
      case "..":
        if queue:
          queue.pop()
      case "." | "":
        pass
      case _:
        queue.append(dir)
    result = ""
    while queue:
      dir = queue.popleft()
      result += "/" + dir
    return result if result else "/"
