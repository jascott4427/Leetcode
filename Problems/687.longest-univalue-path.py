#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        self.getLongestPath(root)
        return self.longest
    
    def getLongestPath(self, node):
        # If we hit an empty node, just give us 0
        if not node:
            return 0
        
        # Recursively run this process down each path 
        # to get each directions max lines
        left_length = self.getLongestPath(node.left)
        right_length = self.getLongestPath(node.right)

        # Reset variables to track current path amounts
        curr_left = 0
        curr_right = 0

        # We extend the left path by its value + 1 for 
        # the connection between them
        if node.left:
            if node.left.val == node.val:
                curr_left = left_length + 1
        if node.right:
            if node.right.val == node.val:
                curr_right = right_length + 1

        curr_path = curr_right + curr_left

        # This updates the global variable for longest path
        self.longest = max(self.longest, curr_path)

        # However, here we want to return the best direction 
        # for this function to work recursively
        return max(curr_left, curr_right)
        

        

# @lc code=end

