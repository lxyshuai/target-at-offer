# coding=utf-8
"""
输入一个整数数组,判断该数组是不是某二叉树的后序遍历
"""


class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def verify_squence_of_BST1(sequence, sequence_begin, sequence_end):
    """
    sequence_begin是树开始的数
    sequence_end是树结束的下一个数
    """
    if sequence == None or sequence_end > len(sequence) or \
            sequence_begin < 0:
        return False

    # 获取根节点
    root = sequence[sequence_end - 1]

    # 根据二叉搜索树的性质，左孩子的每个结点的值都小于根节点
    left_sub_tree_begin = sequence_begin
    left_sub_tree_end = left_sub_tree_begin
    for left_sub_tree_end in range(sequence_begin, sequence_end):
        if sequence[left_sub_tree_end] > root:
            break

    # 判断是否右孩子的每个结点的值都大于根结点
    right_sub_tree_begin = left_sub_tree_end
    right_sub_tree_end = right_sub_tree_begin
    for right_sub_tree_end in range(right_sub_tree_begin, sequence_end):
        if sequence[right_sub_tree_end] < root:
            return False

    # left_sub_tree_begin是左子树开始的数
    # left_sub_tree_end是左子树结束的下一个数
    # 如果left_sub_tree_begin<left_sub_tree_end,说明还有左子树
    # 如果left_sub_tree_begin==left_sub_tree_end,说明没有左子树了,直接返回True
    if left_sub_tree_begin < left_sub_tree_end:
        is_left_sub_tree_BST = verify_squence_of_BST1(sequence,
                                                      left_sub_tree_begin,
                                                      left_sub_tree_end)
    else:
        is_left_sub_tree_BST = True

    # right_sub_tree_begin是左子树开始的数
    # right_sub_tree_end是左子树结束的下一个数
    # 如果right_sub_tree_begin<right_sub_tree_end,说明还有右子树
    # 如果right_sub_tree_begin==right_sub_tree_end,说明没有右子树了,直接返回True
    if right_sub_tree_begin < right_sub_tree_end:
        is_right_sub_tree_BST = verify_squence_of_BST1(sequence,
                                                       right_sub_tree_begin,
                                                       right_sub_tree_end)
    else:
        is_right_sub_tree_BST = True
    return is_left_sub_tree_BST and is_right_sub_tree_BST


def verify_squence_of_BST2(self, sequence):
    # write code here
    if not sequence:
        return False

    # 获取根节点
    root = sequence[-1]

    # 根据二叉搜索树的性质，左孩子的每个结点的值都小于根节点
    for i in range(len(sequence)):
        if sequence[i] > root:
            break

    # 判断是否右孩子的每个结点的值都大于根结点
    for j in range(i, len(sequence)):
        if sequence[j] < root:
            return False

    left = True
    # i > 0 的时候证明有左孩子
    if i > 0:
        # 递归遍历左孩子
        left = self.VerifySquenceOfBST(sequence[: i])

    right = True
    # 证明有右孩子，通过i的值不在最后一个结点判断，len(sequence) - 1 为sequence的最后一个结点
    if i < len(sequence) - 1:
        right = self.VerifySquenceOfBST(sequence[i: -1])

    return left and right


if __name__ == '__main__':
    node1 = BinaryTreeNode(8)
    node2 = BinaryTreeNode(6)
    node3 = BinaryTreeNode(10)
    node4 = BinaryTreeNode(5)
    node5 = BinaryTreeNode(7)
    node6 = BinaryTreeNode(9)
    node7 = BinaryTreeNode(11)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print verify_squence_of_BST1([5, 12, 11], 0, 3)
    # print verify_squence_of_BST([7, 4, 6, 5], 0, 3)
