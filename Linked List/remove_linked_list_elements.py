# Remove all elements from a linked list of integers that have value val.
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        :time complexity: O(n)
        """
        list = []
        tempNode = head
        while tempNode:
            list.append(tempNode.val)
            tempNode = tempNode.next
        count = list.count(val)

        for i in range(count):
            list.remove(val)
            
        head2 = ListNode(None)
        tempNode2 = head2
        
        for item in list:
            tempNode2.next = ListNode(item)
            tempNode2 = tempNode2.next
        return head2.next