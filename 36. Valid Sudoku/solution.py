class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            rowSet, colSet, gridSet = set(), set(), set()
            for j in range(9):
                colItem = board[i][j]
                rowItem = board[j][i]
                gridItem = board[i/3*3+j/3][(i%3)*3+j%3]
                if (colItem!='.' and colItem in colSet) or (rowItem!='.' and rowItem in rowSet) or (gridItem!='.' and gridItem in gridSet):
                    return False
                rowSet.add(rowItem)
                colSet.add(colItem)
                gridSet.add(gridItem)
        return True
