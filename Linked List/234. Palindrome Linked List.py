# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        visited = []
        while head:
            visited.append(head.val)
            head = head.next
        return visited == visited[::-1]