"""
Problem: 237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next is not None:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None

    # def deleteNode(self, node):
    #     """
    #     :type node: ListNode
    #     :rtype: void Do not return anything, modify node in-place instead.
    #     """
    #     if node.next:
    #         node.val, node.next = node.next.val, node.next.next
