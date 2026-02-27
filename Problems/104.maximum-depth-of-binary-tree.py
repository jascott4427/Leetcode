#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Make the variable we want to update global for recursion to access
        self.max_depth = 0

        # Perform recursive cycle
        self.recursion(root)

        # Get final result after recursion
        return self.max_depth
    
    def recursion(self, node):
        # 1. base case (if we dont have a node or it is null)
        # This ends recursion in step 2 at end of tree
        if not node:
            return 0
        
        # 2. We plan for this loop to work, so go ahead and ask for these depths to compare sides
        left_depth = self.recursion(node.left)
        right_depth = self.recursion(node.right)

        # 3. We add one since we include current node
        current_node_depth = max(left_depth, right_depth) + 1

        # 4. Compare to global maximum
        self.max_depth = max(self.max_depth, current_node_depth)

        # 5. Return current depth for use earlier in Part 2. of recursive function
        return current_node_depth
# @lc code=end

