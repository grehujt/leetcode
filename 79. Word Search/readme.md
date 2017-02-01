# 79. Word Search

## Problem
- Given a 2D board and a word, find if the word exists in the grid.

- The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

> For example, given board =
> 
> [
> 
>   ['A','B','C','E'],
>   
>   ['S','F','C','S'],
>   
>   ['A','D','E','E']
>   
> ]
> 
> word = "ABCCED", -> returns true,
> 
> word = "SEE", -> returns true,
> 
> word = "ABCB", -> returns false.

## Solution
```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def _bt(i, j, idx):
            if idx == len(word):
                return True
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!=word[idx]:
                return False
            board[i][j] = '*'  # avoid reuse
            ret = _bt(i-1, j, idx+1) or _bt(i+1, j, idx+1) or _bt(i, j-1, idx+1) or _bt(i, j+1, idx+1)
            board[i][j] = word[idx]  # resume
            return ret
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if _bt(row, col, 0):
                    return True
        return False
```
