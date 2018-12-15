# coding=utf-8
"""
题目一：二叉树的深度
"""


class Solution(object):
    def tree_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.tree_depth(root.left), self.tree_depth(root.right))


"""
题目二：平衡二叉树
"""


class Solution(object):
    def is_balanced(self, root):
        def tree_depth(root):
            if root is None:
                return 0
            return 1 + max(tree_depth(root.left), tree_depth(root.right))

        if root is None:
            return True
        left_depth = tree_depth(root.left)
        right_depth = tree_depth(root.right)
        if abs(right_depth - left_depth) > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)


class Solution(object):
    def is_balanced(self, root):
        def postorder_travesal(root):
            if root is None:
                return 0
            left_depth = postorder_travesal(root.left)
            right_depth = postorder_travesal(root.right)
            if abs(right_depth - left_depth) > 1:
                self.count += 1
            return 1 + max(left_depth, right_depth)

        self.count = 0
        return self.count == 0
