from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # check horizontally
    for i in range(9):
      appear = set()
      for j in range(9):
        if board[i][j] == ".":
          continue
        if board[i][j] in appear:
          return False
        appear.add(board[i][j])
    # check vertically
    for j in range(9):
      appear = set()
      for i in range(9):
        if board[i][j] == ".":
          continue
        if board[i][j] in appear:
          return False
        appear.add(board[i][j])
    # check square
    for a in range(0, 9, 3):
      for b in range(0, 9, 3):
        appear = set()
        for i in range(3):
          for j in range(3):
            if board[a+i][b+j] == ".":
              continue
            if board[a+i][b+j] in appear:
              return False
            appear.add(board[a+i][b+j])
    return True
