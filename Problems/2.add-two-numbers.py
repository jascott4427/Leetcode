#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = self.linkedListToInt(l1)
        num2 = self.linkedListToInt(l2)
        num3 = num1 + num2
        return self.intTolinkedList(num3)

    def linkedListToInt(self, linkedList):
        # print("LL to int started for: ", linkedList)
        result = 0
        counter = 0
        while linkedList:
            result += linkedList.val * (10**counter)
            # print(result)
            linkedList = linkedList.next
            # print(linkedList)
            counter += 1
        return result
    
    def intTolinkedList(self, num):
        head = ListNode()
        current = head
        while num != 0:
            print(head)
            print(num) 

            current.val = num % 10
            num //= 10
            if num == 0: break

            temp = ListNode()
            current.next = temp
            current = temp
        print(head)
        return head


# @lc code=end

