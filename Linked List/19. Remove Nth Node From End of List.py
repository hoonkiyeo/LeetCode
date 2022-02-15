# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return []
        else:
            faster = slower = head
            for _ in range(n):
                faster = faster.next

            if faster is None:
                return head.next

            while faster.next is not None:
                faster = faster.next
                slower = slower.next

            slower.next = slower.next.next
            return head


