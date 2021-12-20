# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.helper(root)
        return self.count

    def helper(self, root):
        if not root:
            return True

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left and right and (not root.left or root.left.val == root.val) and (
                not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False


