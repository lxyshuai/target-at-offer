class Solution(object):
    def kth_node(self, root):
        def inorder_travesal(root):
            if root is None:
                return
            inorder_travesal(root.left)
            self.result.append(root.val)
            inorder_travesal(root.right)

        def inorder_travesal(root):
            stack = []
            current_node = root
            self.result = []
            while stack or current_node:
                if current_node:
                    stack.append(current_node)
                    current_node = current_node.left
                else:
                    current_node = stack.pop()
                    self.result.append(current_node.val)
                    current_node = current_node.right
