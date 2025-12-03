#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tempMatrix = matrix
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                tempMatrix[i][j] = 
        # Swap matrices
        for i in range(n):
            for j in range(n):
                matrix[i][j] = tempMatrix[i][j]
        return matrix
    
        
# @lc code=end

