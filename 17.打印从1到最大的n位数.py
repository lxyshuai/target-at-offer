# coding=utf-8
"""
题目:
输入数字n,按顺序打印从1到最大的n位十进制数.比如输入3,则打印出1、2、3一直到到最大的3位数999
"""
import sys


def increment(number_char_array):
    # 进位
    carry = 0
    is_overflow = False
    for index in reversed(range(len(number_char_array))):
        number = int(number_char_array[index]) + carry
        if index == len(number_char_array) - 1:
            number += 1
        if number >= 10:
            if index == 0:
                is_overflow = True
            number -= 10
            number_char_array[index] = str(number)
            carry = 1
        else:
            number_char_array[index] = str(number)
            break
    return is_overflow


def print_number_char_array(number_char_array):
    is_begin = False
    for index in range(len(number_char_array)):
        if not is_begin and number_char_array[index] != '0':
            is_begin = True
        if is_begin:
            sys.stdout.write(number_char_array[index])
    print


def print_1_to_max_of_n_digits(n):
    if n <= 0:
        return
    number_char_array = ['0' for _ in range(n)]
    while (not increment(number_char_array)):
        print_number_char_array(number_char_array)


def print_1_to_max_of_n_digits_recursively(n):
    if n <= 0:
        return
    number_char_array = ['0' for _ in range(n)]
    for i in range(10):
        process(number_char_array, n, 0)


def process(number_char_array, length, index):
    if index == length:
        print_number_char_array(number_char_array)
        return
    for i in range(10):
        number_char_array[index] = str(i)
        process(number_char_array, length, index + 1)


if __name__ == '__main__':
    print_1_to_max_of_n_digits_recursively(2)
