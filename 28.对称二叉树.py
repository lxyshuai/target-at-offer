# coding=utf-8
"""
题目：
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一个二叉树和它的镜像一样，那么它是对称的

镜像后的二叉树的先右后左的前序遍历与镜像前的二叉树的前序遍历应该相同
"""


def is_symmetrical(root):
    if not root:
        return True
    return is_symmetrical_process(root, root)


def is_symmetrical_process(root1, root2):
    # 两种遍历走到了结尾
    if not root1 and not root2:
        return True
    # 有其中一种遍历没走到结尾
    if not root1 or not root2:
        return False
    if root1.value != root2.value:
        return False

    return is_symmetrical_process(root1.left, root2.right) and is_symmetrical_process(root1.right, root2.left)
