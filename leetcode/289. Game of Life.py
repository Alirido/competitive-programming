from typing import List

class Solution:
  def gameOfLife(self, board: List[List[int]]) -> None:
    tmp_board = [row[:] for row in board]

    m = len(board)
    n = len(board[0])
    def countLiveNeighbor(i: int, j: int) -> int:
      if i < 0 or i >= m or j < 0 or j >= n:
        return 0
      else:
        return board[i][j]
    def nextState(i: int, j: int) -> int:
      liveNeighbors = 0
      liveNeighbors += countLiveNeighbor(i - 1, j - 1)
      liveNeighbors += countLiveNeighbor(i - 1, j)
      liveNeighbors += countLiveNeighbor(i - 1, j + 1)
      liveNeighbors += countLiveNeighbor(i, j - 1)
      liveNeighbors += countLiveNeighbor(i, j + 1)
      liveNeighbors += countLiveNeighbor(i + 1, j - 1)
      liveNeighbors += countLiveNeighbor(i + 1, j)
      liveNeighbors += countLiveNeighbor(i + 1, j + 1)
      if board[i][j] == 0:
        if liveNeighbors == 3:
          return 1
      else:
        if liveNeighbors < 2:
          return 0
        elif liveNeighbors > 3:
          return 0
      return board[i][j]

    for i in range(m):
      for j in range(n):
        tmp_board[i][j] = nextState(i, j)
    
    for i in range(m):
      for j in range(n):
        board[i][j] = tmp_board[i][j]