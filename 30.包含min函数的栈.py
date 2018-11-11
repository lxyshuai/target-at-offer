# coding=utf-8
"""
在定义栈的数据结构,请在该类型中实现一个能够得到栈的最小元素的min函数.
在该栈中,调用min,push和pop的时间复杂度都是O(1)
"""


class StackWithMin(object):
    def __init__(self):
        self.data_stack = list()
        self.min_stack = list()

    def push(self, value):
        self.data_stack.append(value)
        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]

    def pop(self):
        if self.data_stack:
            self.data_stack.pop(-1)
            self.min_stack.pop(-1)


if __name__ == '__main__':
    s = StackWithMin()
    s.push(3)
    s.push(2)
    s.push(1)
    print s.min()
    s.pop()
    print s.min()
