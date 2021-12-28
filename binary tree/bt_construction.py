# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        curr_node = postorder.pop()
        idx = inorder.index(curr_node)

        right = self.buildTree(inorder[idx+1:], postorder)
        left = self.buildTree(inorder[:idx], postorder)

        return TreeNode(curr_node, left, right)