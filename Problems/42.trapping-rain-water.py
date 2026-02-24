#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        leftIdx = 1
        rightIdx = len(height) - 2

        left = height[leftIdx - 1]
        right = height[rightIdx + 1]

        rain = 0
        print(leftIdx, rightIdx, left, right, rain)

        while leftIdx <= rightIdx:
            if left <= right:
                nextLeft = height[leftIdx]
                if nextLeft <= left:
                    rain += left-nextLeft
                    leftIdx += 1
                else: 
                    left = height[leftIdx]
                    leftIdx += 1
            else:
                nextRight = height[rightIdx]
                if nextRight <= right:
                    rain += right - nextRight
                    rightIdx -= 1
                else:
                    right = height[rightIdx]
                    rightIdx -= 1

        return rain

# @lc code=end

