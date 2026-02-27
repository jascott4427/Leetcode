#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#
import heapq
# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.grid_x = len(heights[0])
        self.grid_y = len(heights)
        target_cell = (self.grid_x - 1, self.grid_y - 1)
        self.target_x = target_cell[0]
        self.target_y = target_cell[1]

        dist = [[float('inf')] * self.grid_x for _ in range(self.grid_y)]
        dist[0][0] = 0

        min_heap = [(0, 0, 0)] # effort, x, y
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            if x== self.target_x and y == self.target_y:
                return effort
            
            north = (0, 1)
            west = (-1, 0)
            south = (0, -1)
            east = (1, 0)
            for dx, dy in [north, south, east, west]:
                nx = dx + x
                ny = dy + y
                if self.isInBounds(nx, ny):
                    curr_effort = abs(heights[ny][nx] - heights[y][x])
                    new_effort = max(effort, curr_effort)
                    if new_effort < dist[ny][nx]:
                        dist[ny][nx] = new_effort
                        new_heap = (new_effort, nx, ny)
                        heapq.heappush(min_heap, new_heap)



    def isInBounds(self, x, y):
        if x >= 0 and x < self.grid_x:
            if y >= 0 and y < self.grid_y:
                return True
        return False
        

# @lc code=end

