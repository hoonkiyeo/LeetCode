# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        else:
            node = head
            visited = set()

            while True:
                if node is None or node.next is None:
                    return None
                if node in visited:
                    break
                visited.add(node)
                node = node.next

        return node
