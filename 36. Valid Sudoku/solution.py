class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = set()
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != '.':
                    rowItem, colItem, gridItem = ('r', i, n), ('c', j, n), (i/3, j/3, n)
                    if rowItem in s or colItem in s or gridItem in s:
                        return False
                    s.add(rowItem)
                    s.add(colItem)
                    s.add(gridItem)
        return True
