# coding=utf-8
"""
复杂链表的复制
"""


class ComplexListNode(object):
    def __init__(self, value, next=None, sibling=None):
        self.value = value
        self.next = next
        self.sibling = sibling


def clone_nodes(head):
    """
    复制原始链表的任意节点N并创建新节点N',再把N'链接到N的后面
    """
    current_node = head
    while current_node:
        clone_node = ComplexListNode(current_node.value)
        clone_node.next = current_node.next
        current_node.next = clone_node
        current_node = clone_node.next


def connect_sibling_nodes(head):
    """
    如果原始链表上的节点N的sibling执行S，则它对应的复制节点N'的sibling执行S的复制节点S'
    """
    current_node = head
    while current_node:
        clone_node = current_node.next
        if current_node.sibling:
            clone_node.sibling = current_node.sibling.next
        else:
            clone_node.sibling = None
        current_node = clone_node.next


def reconnect_nodes(head):
    """
    将第二步得到的链表拆成两个链表，奇数位置上的节点组成原始链表，偶数位置上的节点组成复制出来的节点
    """
    if not head:
        return head
    clone_head = head.next
    origin_current_node = head
    clone_current_node = head.next
    while origin_current_node:
        origin_current_node.next = clone_current_node.next
        if origin_current_node.next:
            origin_current_node = origin_current_node.next
            clone_current_node.next = origin_current_node.next
            clone_current_node = clone_current_node.next
        else:
            origin_current_node = None
            clone_current_node.next = None
    return clone_head


def clone(head):
    clone_nodes(head)
    connect_sibling_nodes(head)
    return reconnect_nodes(head)


if __name__ == '__main__':
    node1 = ComplexListNode(1)
    node2 = ComplexListNode(2)
    node3 = ComplexListNode(3)
    node4 = ComplexListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.sibling = node4
    node3.sibling = node2

    a = clone(node1)
    print a
