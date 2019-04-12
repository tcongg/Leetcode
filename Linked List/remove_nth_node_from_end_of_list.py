# Given a linked list, remove the n-th node from the end of list and return its head.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
            
        newHead = ListNode(None)
        newHead.next = head
        movedNode = newHead
        for _ in range(count - n):
            movedNode = movedNode.next
        movedNode.next = movedNode.next.next
        return newHead.next