# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        # root -> left -> right
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)