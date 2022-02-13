# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        visited = set()
        while True:
            if head is None:
                return False
            visited.add(head)
            head = head.next
            if head in visited:
                break
        return True
