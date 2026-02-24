#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        print(chars)
        leftIdx = 0
        rightIdx = len(chars) - 1
        print(rightIdx)
        leftChar = chars[0]
        rightChar = chars[-1]
        while leftIdx < rightIdx:
            print(leftChar, rightChar)
            print(chars)
            if leftChar in chars[leftIdx+1:]:
                chars.pop(leftIdx)
                leftChar = chars[leftIdx]
                rightIdx = len(chars)-1
            elif rightChar in chars[:rightIdx]:
                chars.pop()
                rightIdx = len(chars) - 1
                rightChar = chars[rightIdx]
                
            else:
                leftIdx += 1
            
            
        return len(chars)
        
# @lc code=end

