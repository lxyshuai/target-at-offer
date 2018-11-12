# coding=utf-8
"""
不分行从上到下打印二叉树
从上到下打印二叉树的每个节点,同一层的节点按照从左到右的顺序打印.
"""


class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_from_top_to_bottom(root):
    if not root:
        return
    queue = list()
    queue.append(root)
    while queue:
        current_node = queue.pop(0)
        print current_node.value
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


if __name__ == '__main__':
    node1 = BinaryTreeNode(8)
    node2 = BinaryTreeNode(8)
    node3 = BinaryTreeNode(7)
    node4 = BinaryTreeNode(9)
    node5 = BinaryTreeNode(2)
    node6 = BinaryTreeNode(4)
    node7 = BinaryTreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7

    print_from_top_to_bottom(node1)
