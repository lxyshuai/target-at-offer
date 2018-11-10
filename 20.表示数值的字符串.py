# coding=utf-8
"""
题目：
请实现一个函数用来判断字符串是否表示数字（包括整数和小数）
"""


def is_numeric(string):
    def scan_unsigned_integer():
        global string_index
        before = string_index
        while string_index < len(string) and string[string_index].isdigit():
            string_index += 1
        return string_index > before

    def scan_signed_integer():
        global string_index
        if string[string_index] in ['+', '-']:
            string_index += 1
        return scan_unsigned_integer()

    global string_index
    if not string:
        return False
    result = scan_signed_integer()
    if string[string_index] == '.':
        string_index += 1
        result = scan_unsigned_integer() or result
    if string[string_index] in ['e', 'E']:
        string_index += 1
        result = result and scan_signed_integer()

    if string_index == len(string):
        return result
    else:
        return False


if __name__ == '__main__':
    string_index = 0
    print(is_numeric('+3.123123e123213'))
