# coding=utf-8
"""
题目:定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头结点
"""


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head):
    pre_node = None
    current_node = head
    next_node = head.next
    while current_node:
        current_node.next = pre_node
        if not next_node:
            return current_node
        pre_node = current_node
        current_node = next_node
        next_node = next_node.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    reverse_list(node1)
