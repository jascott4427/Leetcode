#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 0 <= query_glass <= query_row < 100
        row = query_row
        col = query_glass
        tower = self.buildTower()
        tower[0][0] += poured
        for i in range(100):
            for j in range(i+1):
                val = tower[i][j]
                if val > 1.0:
                    overflow = val - 1.0
                    # print(overflow)
                    tower[i][j] = 1.0
                    left = (i+1, j)
                    right = (i+1, j+1)
                    if self.isValid(left):
                        tower[i+1][j] += overflow / 2
                    if self.isValid(right):
                        tower[i+1][j+1] += overflow / 2
                if i == row and j == col:
                    # print("success: ", tower)
                    return tower[row][col]
        # print("failure: ", tower)
        return tower[row][col]

    def isValid(self, tuple):
        row, col = tuple[0], tuple[1]
        if row > 99 or row < 0 or col < 0 or col > row:
            return False
        return True

    def buildTower(self):
        # minGlass = 0
        maxGlass = 99
        tower = []
        for i in range(maxGlass+1):
            row  = []
            for _ in range(i+1):
                row.append(0.0)
            tower.append(row)
        return tower

# @lc code=end

