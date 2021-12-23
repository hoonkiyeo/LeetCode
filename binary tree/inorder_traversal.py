class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # left -> root -> right
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
