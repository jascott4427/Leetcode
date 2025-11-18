#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        forNum = x
        backNum = 0
        while forNum > 0:
            backNum *= 10
            backNum += forNum % 10
            forNum //= 10
        if x == backNum:
            return True
        else:
            # print(forNum, backNum)
            return False
        
# @lc code=end