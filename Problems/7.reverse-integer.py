#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rangeMin = -(2 ** 31)
        rangeMax = (2 **31) - 1
        result = 0
        posX = abs(x)
        while posX > 0:
            result *= 10
            result += posX % 10
            posX //= 10
        result *= self.sign(x)
        if result < rangeMin or result > rangeMax: return 0
        return result
    
    def sign(self, num):
        return -1 if num < 0 else (1)

        
        
# @lc code=end

