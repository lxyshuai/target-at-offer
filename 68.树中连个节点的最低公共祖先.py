# coding=utf-8
"""
树种的两个节点的最低公共祖先
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
二叉树是BST
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        手画出BST，可以得到规律第一个节点p<=val<=q就是结果
        """

        def process(root):
            if root is None:
                return
            if p <= root.val <= q:
                return root
            else:
                if root.val < p:
                    return process(root.right)
                elif root.val > q:
                    return process(root.left)


"""
二叉树是普通二叉树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        # Variable to store LCA node.
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        利用先序遍历遍历，在每个节点判断left,right,middle
        """

        def process(root):
            if root is None:
                return False
            left = process(root.left)
            right = process(root.right)
            middle = root is p or root is q
            if left + right + middle == 2:
                self.result = root
            return left or right or middle

        process(root)
        return self.result
