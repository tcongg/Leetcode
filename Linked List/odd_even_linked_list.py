# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        if head is None or head.next is None:
            return head
        else:
            list = []
            evenList = []
            oddList = []
            while head:
                list.append(head.val)
                head = head.next
                
            i,j = 0,1
            while i < len(list):
                evenList.append(list[i])
                i += 2
            while j < len(list):
                oddList.append(list[j])
                j += 2
        
            tempHead = ListNode(None)
            temp = tempHead
            for item in evenList:
                temp.next = ListNode(item)
                temp = temp.next
            for item in oddList:
                temp.next = ListNode(item)
                temp = temp.next
            return tempHead.next