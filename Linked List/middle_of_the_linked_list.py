# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.
# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :time complexity: O(n)
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        i = 0
        while i < count / 2:
            head = head.next
            i += 1
        
        return head