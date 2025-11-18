#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        exceptions = {"V":"I", "X":"I", "L":"X","C":"X","D":"C","M":"C"}
        letters = list(s)
        print(letters)
        while letters:
            l2 = letters[-1]
            try:
                l1 = letters[-2]
                print(l2, l1)
                print(exceptions[l2])
                if exceptions[l2] == l1:
                    result += values[l2]-values[l1]
                    letters.pop()
                    letters.pop()
                    print(letters)
                else:
                    result += values[l2]
                    letters.pop()
                    print(letters)
            except:
                result += values[l2]
                letters.pop()
        return result

        
# @lc code=end

