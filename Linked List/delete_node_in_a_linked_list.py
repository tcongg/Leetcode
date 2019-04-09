# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Given linked list -- head = [4,5,1,9], which looks like following: 4 -> 5 -> 1 -> 9
# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        :time complexity: O(1)
        """

        node.val = node.next.val
        node.next = node.next.next