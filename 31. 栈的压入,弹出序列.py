# coding=utf-8
"""
输入两个整数序列,第一个序列表示栈的压入顺序,请判断第二个序列是否为该栈的弹出顺序.
假设压入栈的所有数字均不相等
"""


def is_pre_order(push_array, pop_array):
    length = len(push_array)
    stack = list()
    while length:
        if stack:
            # 如果下一个弹出的数字刚好是栈顶的数字,那么直接弹出
            if stack[-1] == pop_array[0]:
                stack.pop(-1)
                pop_array.pop(0)
                length -= 1
            # 如果下一个弹出的数字不在栈顶,则把压栈序列中还没有入栈的数字压入辅助栈,
            # 直到把下一个需要弹出的数字压入栈顶
            else:
                while push_array and stack[-1] != pop_array[0]:
                    stack.append(push_array.pop(0))
                if stack[-1] == pop_array[0]:
                    stack.pop(-1)
                    pop_array.pop(0)
                    length -= 1
                else:
                    break
        else:
            stack.append(push_array.pop(0))

    if pop_array:
        return False
    else:
        return True


if __name__ == '__main__':
    print is_pre_order([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
