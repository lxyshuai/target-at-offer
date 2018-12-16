# coding=utf-8
"""
题目一：翻转单词顺序
"""


class Solution(object):
    def reverse_sentence(self, string):
        def reverse(begin, end):
            while begin < end:
                string_list[begin], string_list[end] = string_list[end], string_list[begin]
                begin += 1
                end -= 1

        if not string:
            return
        string_list = list(string)
        reverse(0, len(string_list) - 1)

        begin = 0
        end = 0
        while end < len(string_list):
            if string_list[end] == ' ':
                reverse(begin, end - 1)
                begin = end + 1
                end = begin
            else:
                end += 1
        return ''.join(string_list)


print Solution().reverse_sentence('I am you')

"""
题目二：左旋转字符串
"""


class Solution(object):
    def left_rotate_string(self, string, n):
        def reverse(begin, end):
            while begin < end:
                string_list[begin], string_list[end] = string_list[end], string_list[begin]
                begin += 1
                end -= 1

        if not string:
            return
        string_list = list(string)
        reverse(0, n - 1)
        reverse(n, len(string_list) - 1)
        reverse(0, len(string_list) - 1)
        return ''.join(string_list)


print Solution().left_rotate_string('abcdefg', 2)
