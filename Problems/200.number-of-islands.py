#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0
        self.grid_x = len(grid[0])
        self.grid_y = len(grid)
        self.grid = grid
        for x in range(self.grid_x):
            for y in range(self.grid_y):
                if self.grid[y][x] == "1":
                    self.islands += 1
                    self.recursion((x, y))
        return self.islands
    
    def recursion(self, tile):
        # Base case
        if not self.isInBounds(tile):
            return
        
        x, y = tile
        left = (x - 1, y)
        right = (x + 1, y)
        up = (x, y + 1)
        down = (x, y - 1)
        directions = [left, right, up, down]
        for direction in directions:
            dx, dy = direction[0], direction[1]
            if self.isInBounds(direction) and self.grid[dy][dx] == "1":
                self.grid[dy][dx] = "0"
                self.recursion(direction)
        
    def isInBounds(self, tile):
        x, y = tile
        if x < 0 or x >= self.grid_x or y < 0 or y>= self.grid_y:
            return False
        return True

        
        
# @lc code=end

