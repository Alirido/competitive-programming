from collections import deque
from typing import List

class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)

    def label_to_cell(label: int) -> int:
      # Map 1-indexed label to board[r][c], reading bottom-up in boustrophedon order
      r, c = divmod(label - 1, n)
      row = n - 1 - r
      col = c if r % 2 == 0 else n - 1 - c
      return board[row][col]

    target = n * n
    visited = {1}
    queue = deque([(1, 0)])    # (square, moves)

    while queue:
      square, moves = queue.popleft()
      if square == target:
        return moves

      for d in range(1, 7):
        next_square = square + d
        if next_square > target:
          break
        # If this square has a snake or ladder, take it
        dest = label_to_cell(next_square)
        if dest == -1:
          dest = next_square
        if dest not in visited:
          visited.add(dest)
          queue.append((dest, moves + 1))

    return -1
