from collections import deque
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        
        q = deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            left = q.popleft()
            right = q.popleft()

            if right is None and left is None:
                pass
            elif left.val != right.val or right is None or left is None:
                return False
            
            if left and right:
                q.append(left.left)
                q.append(right.right)
                q.append(left.right)
                q.append(right.left)

        return True


# @lc code=end

