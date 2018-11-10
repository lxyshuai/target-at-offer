# coding=utf-8
"""
题目:
请完成一个函数，输入一棵二叉树，该函数输出它的镜像
"""


def mirror_recursively(root):
    if not root:
        return
    if not root.left and not root.right:
        return

    root.left, root.right = root.right, root.left
    if root.left:
        mirror_recursively(root.left)
    if root.right:
        mirror_recursively(root.right)
