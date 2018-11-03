# coding=utf-8
"""
题目:用两个栈实现一个队列
"""


class Queue(object):
    def __init__(self):
        self.push_stack = list()
        self.pop_stack = list()

    def push(self, value):
        self.push_stack.append(value)

    def pop(self):
        if self.pop_stack:
            return self.pop_stack.pop()
        else:
            if not self.push_stack:
                raise Exception
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()


"""
用两个队列实现一个栈
"""


class Stack(object):
    def __init__(self):
        self.queue = list()
        self.help_queue = list()

    def add(self, value):
        self.queue.append(value)

    def pop(self):
        while len(self.queue) != 1:
            self.help_queue.append(self.queue.pop(0))
        pop_value = self.queue.pop()
        self.queue, self.help_queue = self.help_queue, self.queue
        return pop_value


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.pop()

    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    print s.pop()