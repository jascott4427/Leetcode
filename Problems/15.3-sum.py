#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lenNums = len(nums)
        target = 0
        sortedNums = sorted(nums)
        results = []

        for i in range(lenNums)
            i_val = sortedNums[i]
            diff = target - i_val

            leftIdx = 0
            rightIdx = lenNums - 1

            while leftIdx < rightIdx:
                left = sortedNums[leftIdx]
                right = sortedNums[rightIdx]
                if i == leftIdx or i == rightIdx:
                    continue
                if left + right == diff:
                    results.append(sorted([i_val, left, right]))

                


# @lc code=end

