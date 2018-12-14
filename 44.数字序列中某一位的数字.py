# coding=utf-8
"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一个函数，求任意第n位对应的数字。
"""


class Solution(object):
    def digit_at_index(self, index):
        def count_of_integers(digits):
            """
            得到digits位数总共有多少个
            @param digits:
            @type digits:
            @return:
            @rtype:
            """
            if digits == 1:
                return 10
            count = 10 ** (digits - 1)
            return 9 * count

        def begin_number(digits):
            """
            得到digits位数开头的第一个数字
            @param digits:
            @type digits:
            @return:
            @rtype:
            """
            if digits == 1:
                return 0
            return 10 ** (digits - 1)

        def digit_at_index(index, digits):
            # 求出该位置处于digits位数中的哪个数,比如 881位于370这个3位数位置中
            number = begin_number(digits) + index / digits
            # 求出该位置在该数中的位置,比如881位于370这个3位数中的从左边数的第一个位置
            index_of_number = index % digits
            return int(str(number)[index_of_number])

        if index < 0:
            return -1
        digits = 1
        while True:
            numbers = count_of_integers(digits)
            if index < numbers * digits:
                return digit_at_index(index, digits)
            index -= numbers * digits
            digits += 1


if __name__ == '__main__':
    print Solution().digit_at_index(1001)
