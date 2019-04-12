# Given a linked list, determine if it has a cycle in it.
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        reverse = self.reverseList(head)
        if reverse is head:
            return True
        else:
            return False
        
    def reverseList(self, head):
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp    
        return new_head