# coding=utf-8
"""
输入某二叉树前序遍历和中序遍历,重建该二叉树
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct(preorder_traversal, inorder_traversal):
    return process(preorder_traversal, inorder_traversal)


def process(preorder_traversal, inorder_traversal):
    # 前序遍历为空,说明为空节点
    if len(preorder_traversal) == 0:
        return None
    root = Node(preorder_traversal[0])
    root_index_in_inorder_traversal = inorder_traversal.index(
        preorder_traversal[0])
    root.left = process(
        preorder_traversal[1:root_index_in_inorder_traversal + 1],
        inorder_traversal[0: root_index_in_inorder_traversal]
    )
    root.right = process(
        preorder_traversal[root_index_in_inorder_traversal + 1:],
        inorder_traversal[root_index_in_inorder_traversal + 1:]
    )
    return root


if __name__ == '__main__':
    root = construct([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    print 1
