#
# @lc app=leetcode id=292 lang=python
#
# [292] Nim Game
#

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxTake = 3
        if n % (maxTake + 1) == 0:
            return False
        return True

        
# @lc code=end

