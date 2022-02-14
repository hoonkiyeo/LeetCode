# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA and not headB:
            return None
        nodeA = headA
        nodeB = headB
        visited = set()

        while nodeA is not None:
            visited.add(nodeA)
            nodeA = nodeA.next

        while nodeB is not None:
            if nodeB in visited:
                return nodeB
            else:
                nodeB = nodeB.next
        return None