# coding=utf-8
"""
给定一棵二叉树和其中一个节点,如何找出中序遍历序列的下一个节点
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def link(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent


def get_next(target):
    if not target:
        return
    # 如果该节点有右子树,则下一个节点是右子树的最左节点
    if target.right:
        right_tree = target.right
        while right_tree.left:
            right_tree = right_tree.left
        return right_tree
    # 如果该节点没有右子树,如果该节点是父节点的左子节点,则下一个节点是该节点的父节点
    elif target.parent:
        current_node = target
        parent_node = target.parent
        while parent_node and current_node == parent_node.right:
            current_node = parent_node
            parent_node = current_node.parent
        return parent_node


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.link(b, c, None)
    b.link(d, e, a)
    c.link(f, g, a)
    d.link(None, None, b)
    e.link(h, i, b)
    f.link(None, None, c)
    g.link(None, None, c)
    h.link(None, None, e)
    i.link(None, None, e)
    print get_next(g).value
