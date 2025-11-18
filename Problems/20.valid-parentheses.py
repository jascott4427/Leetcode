#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"(":")", "{":"}","[":"]"}
        expected = ""
        for char in s:
            pair = ""
            if char in pairs:
                pair = pairs[char]
                expected = ''.join([pair, expected])
                #print("Step 1", char, expected)
            elif expected != "" and char == expected[0]:
                expected = expected[1:]
                #print("Step 2", char, expected)
            else:
                return False
                #print("Step 3", char, expected)
        
        if expected != "": return False
        return True

# @lc code=end

