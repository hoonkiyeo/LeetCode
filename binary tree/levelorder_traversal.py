class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        levels = []
        if not root:
            return []
        def traverse(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)

        traverse(root, 0)
        return levels





