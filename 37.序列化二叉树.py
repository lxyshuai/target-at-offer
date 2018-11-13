# coding=utf-8
"""
请实现两个函数，分别用来序列化和反序列化二叉树
"""
from collections import deque


class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialize(root):
    if not root:
        print '$'
    print root.value
    serialize(root.left)
    serialize(root.right)


def deserialize(string):
    char_array = deque(list(string))

    def process():
        if char_array:
            char = char_array.popleft()
            if char == '$':
                return None
            root = BinaryTreeNode(char)
            root.left = process()
            root.right = process()
            return root
        return process()


