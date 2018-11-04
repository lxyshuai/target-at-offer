# coding=utf-8
"""
题目:请设计一个函数,用来判断一个矩阵中是否存在一条包含某字符串所有字符的路径
"""


def has_path_core(row, column, matrix, rows, columns, string, visited_matrix):
    # basecase
    if len(string) == 0:
        return True

    has_path = False
    if (
            0 <= row < rows
            and 0 <= column < columns
            and not visited_matrix[row][column]
            and matrix[row][column] == string[0]
    ):
        visited_matrix[row][column] = True
        has_path = has_path_core(row, column + 1, matrix, rows, columns, string[1:], visited_matrix) or \
                   has_path_core(row, column - 1, matrix, rows, columns, string[1:], visited_matrix) or \
                   has_path_core(row + 1, column, matrix, rows, columns, string[1:], visited_matrix) or \
                   has_path_core(row - 1, column, matrix, rows, columns, string[1:], visited_matrix)
        if not has_path:
            visited_matrix[row][column] = False
    return has_path


def has_path(matrix, string):
    if not matrix:
        return False
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    visited_matrix = [[False for _ in range(columns)] for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            if has_path_core(row, column, matrix, rows, columns, string,
                             visited_matrix):
                return True
    return False


if __name__ == '__main__':
    matrix = [
        ['a', 'b', 't', 'g'],
        ['c', 'f', 'c', 's'],
        ['j', 'd', 'e', 'h'],
    ]
    print has_path(matrix, 'abfb')
