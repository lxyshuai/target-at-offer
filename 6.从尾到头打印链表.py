# coding=utf-8
"""
从尾到头打印链表
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list_reversingly_iteratively(head):
    if not head:
        return
    print_list_reversingly_iteratively(head.next)
    print head.value


if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    print_list_reversingly_iteratively(node1)
