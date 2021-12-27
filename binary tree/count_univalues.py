# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        self.count = 0
        self.countuni(root)
        return self.count

    def countuni(self, root):
        if not root:
            return True

        left = self.countuni(root.left)
        right = self.countuni(root.right)

        if left == False or right == False
            return False
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False

        self.count += 1
        return True



