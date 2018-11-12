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
        print current_node.value,
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


"""
题目二:分行从上到下打印二叉树
从上到下按层打印二叉树,同一层的节点按从左到右的顺序打印,每一层打印一行.
"""


def print_form_top_to_bottom_split_row(root):
    if not root:
        return
    queue = list()
    queue.append(root)
    next_level_count = 0
    this_level_count = 1
    while queue:
        current_node = queue.pop(0)
        print current_node.value,
        this_level_count -= 1
        if current_node.left:
            queue.append(current_node.left)
            next_level_count += 1
        if current_node.right:
            queue.append(current_node.right)
            next_level_count += 1
        if this_level_count == 0:
            print
            this_level_count = next_level_count
            next_level_count = 0


"""
之字形打印二叉树
"""


def print_form_top_to_bottom_zig(root):
    if not root:
        return
    direction = True
    this_level_stack = list()
    next_level_stack = list()
    this_level_stack.append(root)
    while this_level_stack:
        # 方向
        current_node = this_level_stack.pop()
        print current_node.value
        if direction:
            if current_node.left:
                next_level_stack.append(current_node.left)
            if current_node.right:
                next_level_stack.append(current_node.right)
        else:
            if current_node.right:
                next_level_stack.append(current_node.right)
            if current_node.left:
                next_level_stack.append(current_node.left)

        if not this_level_stack:
            this_level_stack, next_level_stack = next_level_stack, this_level_stack
            direction = not direction


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

    print_form_top_to_bottom_zig(node1)
