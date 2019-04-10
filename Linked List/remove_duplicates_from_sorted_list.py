# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Example:
# Input: 1->1->2->3->3
# Output: 1->2->3
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tempNode = head
        if tempNode is None:
            return head
        
        while tempNode.next:
            if tempNode.val == tempNode.next.val:
                tempNode.next = tempNode.next.next
            else:
                tempNode = tempNode.next        
        return head