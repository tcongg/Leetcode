# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        :time complexity: O(n)
        """
        list = []
        while l1:
            list.append(l1.val)
            l1 = l1.next
        
        while l2:
            list.append(l2.val)
            l2 = l2.next
            
        list.sort()
        
        head = ListNode(None)
        temp = head
        for item in list:
            temp.next = ListNode(item)
            temp = temp.next
        return head.next