# coding=utf-8
"""
题目：
输入一个矩阵，按照以外向里以顺时针的顺序依次打印出每一个数字
"""


def print_matrix_spiral_order(matrix):
    if not matrix:
        return
    top_row = 0
    top_column = 0
    down_row = len(matrix) - 1
    down_column = len(matrix[0]) - 1 if len(matrix) else 0

    while top_row <= down_row and top_column <= down_column:
        print_edge(matrix, top_row, top_column, down_row, down_column)
        top_row += 1
        top_column += 1
        down_row -= 1
        down_column -= 1


def print_edge(matrix, top_row, top_column, down_row, down_column):
    # 在同一row
    if top_row == down_row:
        for column in range(top_column, down_column + 1):
            print matrix[top_row][column]
    # 在同一column
    elif top_column == down_column:
        for row in range(top_row, down_row + 1):
            print matrix[row][top_column]
    # 不在同一行且不在同一列
    else:
        current_row = top_row
        current_column = top_column
        # 上边
        while current_column < down_column:
            print matrix[current_row][current_column]
            current_column += 1
        # 右边
        while current_row < down_row:
            print matrix[current_row][current_column]
            current_row += 1
        # 下边
        while current_column > top_column:
            print matrix[current_row][current_column]
            current_column -= 1
        # 左边
        while current_row > top_row:
            print matrix[current_row][current_column]
            current_row -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    # matrix = [range(1, 4), range(4, 7), range(7, 10), range(10, 13), range(13, 16)]
    print_matrix_spiral_order(matrix)
