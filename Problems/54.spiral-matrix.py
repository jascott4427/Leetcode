#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        if m < 1: return matrix
        if n > 10: return matrix

        result = []
        rowsSeen = []
        colsSeen = []

        done = False
        i = 0
        j = 0
        direction = (0, 1)
        colsDone = []
        rowsDone = []
        while not done:
            result.append(matrix[i][j])
            projCell = (i+direction[0],j+direction[1])
            # print(projCell, rowsDone, colsDone)
            # print(not self.isValid(projCell,m,n))
            # print(projCell[0] in rowsDone)
            # print(projCell[1] in colsDone)

            if not self.isValid(projCell, m, n) or projCell[0] in rowsDone or projCell[1] in colsDone:
                if direction == (1,0): 
                    direction = (0,-1)
                    colsDone.append(j)
                elif direction == (0,-1): 
                    direction = (-1,0)
                    rowsDone.append(i)
                elif direction == (-1,0): 
                    direction = (0,1)
                    colsDone.append(j)
                elif direction == (0,1): 
                    direction = (1,0)
                    rowsDone.append(i)

            projCell = (i+direction[0],j+direction[1])
            # print(projCell, rowsDone, colsDone)
            # print(not self.isValid(projCell,m,n))
            # print(projCell[0] in rowsDone)
            # print(projCell[1] in colsDone)
            if not self.isValid(projCell, m, n) or projCell[0] in rowsDone or projCell[1] in colsDone:
                done = True
            i += direction[0]
            j += direction[1]
        return result
    
    def isValid(self, cell, m, n):
        if cell[0] >= m or cell[1]>=n or cell[0]<0 or cell[1]<0:
            return False
        return True
        
# @lc code=end

