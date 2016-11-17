class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def bt(boards, tmpBoard, r, cBools, diag1Bools, diag2Bools):
            if r == n:
                boards.append([''.join(row) for row in tmpBoard])
                return
            for c in range(n):
                d1, d2 = (r+c) % const, (r-c+const) % const
                if not cBools[c] and not diag1Bools[d1] and not diag2Bools[d2]:
                    cBools[c], diag1Bools[d1], diag2Bools[d2] = True, True, True
                    tmpBoard[r][c] = 'Q'
                    bt(boards, tmpBoard, r+1, cBools, diag1Bools, diag2Bools)
                    tmpBoard[r][c] = '.'
                    cBools[c], diag1Bools[d1], diag2Bools[d2] = False, False, False
        boards = []
        const = (n << 1) - 1
        bt(boards, [['.']*n for _ in range(n)], 0, [False]*n, [False]*const, [False]*const)
        return boards

Solution().solveNQueens(4)
