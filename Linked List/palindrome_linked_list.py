# Given a singly linked list, determine if it is a palindrome.
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head:
            list.append(head.val)
            head = head.next
        
        revList = list[::-1]
        for i in range(len(list)):
            if list[i] != revList[i]:
                return False
        return True