# coding=utf-8
"""
题目:
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯:从1开始计数
"""


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def find_kth_to_tail(head, k):
    if not head and k == 0:
        return
    fast = head
    slow = head
    for _ in range(k):
        if fast.next:
            fast = fast.next
        else:
            return
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    print (node1, 2)
