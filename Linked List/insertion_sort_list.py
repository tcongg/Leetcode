# Sort a linked list using insertion sort.
# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = []
        while head:
            list.append(head.val)
            head = head.next
        self.insertionSort(list)
        
        newHead = ListNode(None)
        temp = newHead
        for item in list:
            temp.next = ListNode(item)
            temp = temp.next
        return newHead.next
    
    def insertionSort(self, arr): 
        for i in range(1, len(arr)): 
            key = arr[i] 
            j = i-1
            while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
            arr[j + 1] = key 