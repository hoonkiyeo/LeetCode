class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    #perfect binary tree
    def connect(self, root):
        if not root:
            return None

        if root.right:
            if root.left:
                root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
                
        root.left = self.connect(root.left)
        root.right = self.connect(root.right)
        return root
