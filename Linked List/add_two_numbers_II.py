# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1 = []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        str1 = [str(i) for i in arr1]
        num1 = int(''.join(str1))
        
        arr2 = []
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        str2 = [str(i) for i in arr2]
        num2 = int(''.join(str2))
        
        sum = str(num1 + num2)
        
        head = ListNode(None)
        temp = head
        for item in sum:
            temp.next = ListNode(item)
            temp = temp.next
        return head.next