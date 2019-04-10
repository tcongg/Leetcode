# Write a program to find the node at which the intersection of two singly linked lists begins.
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA = []
        while headA:
            listA.append(headA)
            headA = headA.next
            
        listB = []
        while headB:
            listB.append(headB)
            headB = headB.next

        intersecVal = None
        while len(listA) != 0 and len(listB) != 0:
            valA = listA.pop()
            valB = listB.pop()
            if valA == valB:
                intersecVal = valA
            else:
                break
        return intersecVal