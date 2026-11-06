class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    seen = set()

    for i in range(9):
      for j in range(9):
        val = board[i][j]
        if val == ".":
          continue

        row_id = f"row_{i}_{val}"
        col_id = f"col_{j}_{val}"
        box_id = f"box_{i//3}_{j//3}_{val}"

        if row_id in seen or col_id in seen or box_id in seen:
          return False

        seen.add(row_id)
        seen.add(col_id)
        seen.add(box_id)

    Thunder_return = True
    return True
