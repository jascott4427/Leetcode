#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorts each item x in the array by the x[0] or start time
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        for interval in intervals:
            start = interval[0]
            finish = interval[1]
            if merged_intervals == []:
                merged_intervals.append(interval)
            elif start <= merged_intervals[-1][1]:
                new_finish = max(finish, merged_intervals[-1][1])
                merged_intervals[-1][1] = new_finish
            else:
                merged_intervals.append(interval)

        return merged_intervals
# @lc code=end

