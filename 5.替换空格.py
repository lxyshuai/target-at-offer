# coding=utf-8
"""
题目:请实现一个函数,将字符串中的每个空格替换成成"%20".
"""


def replace_blank(string):
    char_array = list(string)
    number_of_blank = 0
    for char in char_array:
        if char == " ":
            number_of_blank += 1
    new_length = len(char_array) + number_of_blank * 2
    result = [0 for _ in range(new_length)]
    index_of_new = new_length - 1
    index_of_original = len(char_array) - 1
    while index_of_original >= 0:
        if char_array[index_of_original] == " ":
            result[index_of_new] = '0'
            index_of_new -= 1
            result[index_of_new] = '2'
            index_of_new -= 1
            result[index_of_new] = '%'
            index_of_new -= 1
        else:
            result[index_of_new] = char_array[index_of_original]
            index_of_new -= 1
        index_of_original -= 1
    return result

if __name__ == '__main__':
    print replace_blank("we are happy.")
