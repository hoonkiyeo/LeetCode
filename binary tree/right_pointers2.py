from collections import deque
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution(object):
    def connect(self, root):
        q = deque()
        if not root:
            return root
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
