#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        curr1 = list1
        curr2 = list2
        while curr1 or curr2:
            lastNode = ListNode()
            if curr1 and curr2:
                if curr1 >= curr2:
                    lastNode.val = curr1.val
                    head.next = lastNode
                elif curr2 >= curr1:
                    head.val = curr2.val


        
# @lc code=end

