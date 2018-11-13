# coding=utf-8
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表
"""


class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Soulution():
    def __init__(self):
        self.last_node_in_list = None

    def convert(self, root):
        def convert_node(root):
            # 如果遍历到空节点，不处理直接返回
            if not root:
                return
            # 如果遍历到不是空节点
            else:
                # 如果节点有左子树,递归调整左子树
                if root.left:
                    convert_node(root.left)

                # root的left指向self.last_node_in_list
                root.left = self.last_node_in_list
                # self.last_node_in_list的right指向root,self.last_node_in_list有可能为None
                if self.last_node_in_list:
                    self.last_node_in_list.right = root

                # 该节点成为self.last_node_in_list
                self.last_node_in_list = root
                if root.right:
                    convert_node(root.right)
            return self.last_node_in_list

        convert_node(root)
        head = self.last_node_in_list
        while head and head.left:
            head = head.left
        return head


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

    result = Soulution().convert(node1)
    print result
