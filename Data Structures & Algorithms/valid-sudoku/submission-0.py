class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        box = {}
        for r in range(9):
            rows[r] = set()
        for c in range(9):
            cols[c] = set()
        for b in range(9):
            box[b] = set()
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                bo = (r // 3)* 3 + (c//3)
                if num in rows[r] or num in cols[c] or num in box[bo]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                box[bo].add(num)
        return True