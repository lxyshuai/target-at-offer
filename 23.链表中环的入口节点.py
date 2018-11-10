# coding=utf-8
"""
题目:
如果一个链表中包含环，如何找到入环节点
"""


def find_meeting_node(head):
    if not head:
        return
    slow = head
    fast = head
    while True:
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            return None
        slow = slow.next
        if fast == slow:
            return fast


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def entry_node_of_loop(head):
    meeting_node = find_meeting_node(head)
    if not meeting_node:
        return None

    # 找到环中的节点数量
    count = 1
    current_node = meeting_node
    while current_node.next != meeting_node:
        current_node = current_node.next
        count += 1

    first_node = head
    second_node = head
    for _ in range(count):
        second_node = second_node.next

    while first_node != second_node:
        first_node = first_node.next
        second_node = second_node.next

    return first_node


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = node1.next
    print entry_node_of_loop(node1)
