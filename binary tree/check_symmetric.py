# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        return self.helper(root, root)
    def helper(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        return root1.val == root2.val and self.helper(root1.left, root2.right) and self.help(root1.right, root2.left)
