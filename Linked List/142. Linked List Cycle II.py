# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        node = head
        visited = set()

        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None