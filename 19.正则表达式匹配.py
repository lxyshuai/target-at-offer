# coding=utf-8
"""
题目：
请实现一个函数用来匹配包含'.'和'*'的正则表达式
"""


def process(string, string_index, pattern, pattern_index):
    # basecase
    if string_index == len(string) and pattern_index == len(pattern):
        return True
    if string_index != len(string) and pattern_index == len(pattern):
        return False
    if string_index == len(string) and pattern_index != len(pattern):
        return False

    # 当模式的第二字符是'*'时，
    if pattern_index < len(pattern) - 1 and pattern[pattern_index + 1] == '*':
        # 如果模式的第一个字符和字符串的第一个字符相匹配，则在字符串后移一个，而模式有两种选择:可以在模式上向后移动两个字符，也可以保持模式不变
        if pattern[pattern_index] == string[string_index] or pattern[pattern_index] == '.':
            return process(string, string_index, pattern, pattern_index + 2) or \
                   process(string, string_index + 1, pattern, pattern_index) or \
                   process(string, string_index + 1, pattern, pattern_index + 2)
        # 如果模式的第一个字符和字符串的第一个字符不相匹配，在模式上相后移动两个字符,这相当于'*'和前面的字符都被忽略
        else:
            return process(string, string_index, pattern, pattern_index + 2)
    # 当模式的第二字符不是'*'时
    else:
        if pattern[pattern_index] == string[string_index] or pattern[pattern_index] == '.':
            return process(string, string_index + 1, pattern, pattern_index + 1)
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
