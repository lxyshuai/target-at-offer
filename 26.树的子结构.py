# coding=utf-8
"""
题目:
输入两棵二叉树A和B，判断B是不是A的子结构
"""


class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = left
        self.left = right


def has_subtree(root1, root2):
    result = False
    if root1 and root2:
        if root1.value == root2.value:
            result = does_tree1_have_tree2(root1, root2)
        if not result:
            result = has_subtree(root1.left, root2)
        if not result:
            result = has_subtree(root1.right, root2)
    return result


def does_tree1_have_tree2(root1, root2):
    # basecase
    if not root2:
        return True
    if not root1:
        return False
    if root1.value == root2.value:
        return does_tree1_have_tree2(root1.left, root2.left) and does_tree1_have_tree2(root1.right, root2.right)
    else:
        return False


if __name__ == '__main__':
    node1 = BinaryTreeNode(8)
    node2 = BinaryTreeNode(8)
    node3 = BinaryTreeNode(7)
    node4 = BinaryTreeNode(9)
    node5 = BinaryTreeNode(2)
    node6 = BinaryTreeNode(4)
    node7 = BinaryTreeNode(7)
    node1.left = node2
    node2.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7

    node8 = BinaryTreeNode(8)
    node9 = BinaryTreeNode(9)
    node10 = BinaryTreeNode(2)
    node8.left = node9
    node8.right = node10

    print has_subtree(node1, node8)
