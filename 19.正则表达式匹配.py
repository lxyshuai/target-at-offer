# coding=utf-8
"""
题目：
请实现一个函数用来匹配包含'.'和'*'的正则表达式
"""


def process(string, string_index, pattern, pattern_index):
    # basecase
    # string 和 pattern 同时走到最后返回True
    if string_index == len(string) and pattern_index == len(pattern):
        return True
    # string走到最后，但是pattern没有走到最后，返回False
    if string_index == len(string) and pattern_index != len(pattern):
        return False
    # pattern走到最后，但是string没有走到最后，返回False
    if string_index != len(string) and pattern_index == len(pattern):
        return False

    # pattern的第二个字符是'*'
    if pattern_index < len(pattern) - 1 and pattern[pattern_index + 1] == '*':
        # pattern的第一个字符和string相同，或者pattern的第一个字符是'.'
        if string[string_index] == pattern[pattern_index] or pattern[pattern_index] == '.':
            # pattern不变，string往后移一位
            # pattern后移两位，string不往后移
            # pattern后移两位，string往后移一位
            # pattern不变，string往后移一位
            return process(string, string_index + 1, pattern, pattern_index) or \
                   process(string, string_index, pattern, pattern_index + 2) or \
                   process(string, string_index + 1, pattern, pattern_index + 2) or \
                   process(string, string_index + 1, pattern, pattern_index)
        # pattern的第一个字符和string不相同，且pattern的第一个字符不是'.'
        else:
            # pattern后移两位，string不变
            return process(string, string_index, pattern, pattern_index + 2)
    # pattern的第二个字符不是'*'
    else:
        # pattern的第一个字符和string相同，或者pattern的第一个字符是'.'
        if string[string_index] == pattern[pattern_index] or pattern[pattern_index] == '.':
            return process(string, string_index + 1, pattern, pattern_index + 1)
        # pattern的第一个字符和string不相同，且pattern的第一个字符不是'.'
        else:
            return False


def match(string, pattern):
    if not string and not pattern:
        return False
    return process(string, 0, pattern, 0)


if __name__ == '__main__':
    print match('aaa', 'a.a')
    print match('aaa', 'ab*ac*a')
    print match('aaa', 'aa.a')
