# coding=utf-8
"""
输入一棵二叉树和一个整数,打印出二叉树中节点值得和为输入整数的所有路径.
从树的根节点开始往下一只到叶节点所经过的节点形成一条路径
"""


class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_path(root, target_sum):
    if not root:
        return
    find_path_process(root, list(), 0, target_sum)


def find_path_process(root, path, current_sum, target_sum):
    current_sum += root.value
    path.append(root.value)
    # 如果遇到叶节点
    if not root.left and not root.right:
        if current_sum == target_sum:
            for value in path:
                print value,
            print
    else:
        if root.left:
            find_path_process(root.left, path, current_sum, target_sum)
        if root.right:
            find_path_process(root.right, path, current_sum, target_sum)
    path.pop(-1)


def find_path2(root, target_sum):
    if not root and target_sum == 0:
        return True
    elif not root and target_sum != 0:
        return False
    return find_path2(root.left, target_sum - root.value) or \
           find_path2(root.right, target_sum - root.value)


if __name__ == '__main__':
    node1 = BinaryTreeNode(10)
    node2 = BinaryTreeNode(5)
    node3 = BinaryTreeNode(12)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    find_path(node1, 22)
    print find_path2(node1, 22)
