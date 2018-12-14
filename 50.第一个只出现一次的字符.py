# coding=utf-8
"""
在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出'b'。要求时间复杂度为O(n)。
"""


class Solution(object):
    def first_not_repeating_char(self, string):
        appear_dict = {}
        for index, char in enumerate(string):
            if char not in appear_dict:
                appear_dict[char] = 1
            else:
                appear_dict[char] = appear_dict[char] + 1

        for char in string:
            if appear_dict[char] == 1:
                return char


if __name__ == '__main__':
    print Solution().first_not_repeating_char('abaccdeff')
