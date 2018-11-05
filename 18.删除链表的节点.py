# coding=utf-8
"""
题目一:
在O(1)的时间内删除链表节点
给定单向链表的头指针和一个节点指针,定义一个函数在O(1)时间内删除该节点
"""


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(head_node, to_be_delete_node):
    # 链表只有一个节点,删除该节点
    if head_node.next == None:
        head_node = None
        to_be_delete_node = None
    # 链表有多个节点
    else:
        # 要删除的节点是尾节点
        if to_be_delete_node.next == None:
            current_node = head_node
            while current_node.next != to_be_delete_node:
                current_node = current_node.next
            current_node.next = None
        # 要删除的节点不是尾节点
        else:
            next_node = to_be_delete_node.next
            to_be_delete_node.value = next_node.value
            to_be_delete_node.next = next_node.next
            next_node.next = None


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    delete_node(node1, node3)
