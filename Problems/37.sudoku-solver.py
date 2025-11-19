#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.RunBacktracking(board, 0, 0)
        
                            
    def RunBacktracking(self, board, startX, startY):
        n = 9

        # Check if reached beyond last cell
        if startX == 8 and startY == 9:
            return True
        
        # detect changing rows
        if startY == 9:
            startX += 1
            startY = 0

        # Skip non-empty cells
        if not self.CellIsEmpty(board, startX, startY): 
            return self.RunBacktracking(board, startX, startY+1)

        # Check 1-9
        for num in range(n):
            num+=1
            if self.NumIsValid(board, startX, startY, num):
                board[startX][startY] = str(num)
                if self.RunBacktracking(board, startX, startY+1):
                    return True
                board[startX][startY] = "."
                
        return False
                        
    def CellIsEmpty(self, board, x, y):
        if board[x][y] == ".":
            return True
        return False
    
    def NumIsValid(self, board, x, y, num):
        #TODO Make this more efficient
        n = 9
        num = str(num)
        # Check Rows
        for i in range(n):
            if board[i][y] == num:
                return False
        
        # Check Columns
        for j in range(n):
            if board[x][j] == num:
                return False

        # Check Square
        minorRow = x % 3 # 0, 1, 2
        minorCol = y % 3
        startRow = x - minorRow
        startCol = y - minorCol
        for i in range(3):
            for j in range(3):
                if board[i+startRow][j+startCol] == num: 
                    return False

        return True

        
# @lc code=end

