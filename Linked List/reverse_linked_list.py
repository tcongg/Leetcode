# Reverse a singly linked list
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :time complexity: O(n)
        """
        prevNode = None

        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        head = prevNode
        return prevNode