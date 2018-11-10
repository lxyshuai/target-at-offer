# coding=utf-8
"""
题目:
输入两个递增排序的链表，合并这两个链表并使新链表的节点仍然是递增排序
"""


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_recursive(head1, head2):
    # basecase
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.value < head2.value:
        merge_list_head = head1
        merge_list_head.next = merge_recursive(head1.next, head2)
    else:
        merge_list_head = head2
        merge_list_head.next = merge_recursive(head1, head2.next)
    return merge_list_head


def merge_iterative(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    merge_list_head = ListNode(-1)
    merge_list_current_node = merge_list_head
    while head1 and head2:
        if head1.value < head2.value:
            merge_list_current_node.next = head1
            merge_list_current_node = merge_list_current_node.next
            head1 = head1.next
        else:
            merge_list_current_node.next = head2
            merge_list_current_node = merge_list_current_node.next
            head2 = head2.next
    if head1:
        merge_list_current_node.next = head1
    else:
        merge_list_current_node.next = head2
    return merge_list_head.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)

    node2 = ListNode(4)
    node2.next = ListNode(5)
    node2.next.next = ListNode(6)

    print merge_iterative(node1, node2)
    print 1
