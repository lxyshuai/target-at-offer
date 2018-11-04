# coding=utf-8
"""
题目：
地上有个m行n列的方格。一个机器人从坐标(0,0)的格子开始移动，
它每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数
位之和大于k的格子。例如，当k为18时，机器人能够进入方格(35,37)，
因为3+5+3+7=18.但它不能进入方格(35,38)，因为3+5+3+8=19.
请问该机器人能够达到多少格子？
"""


def moving_count_core(rows, columns, row, column, visited_matrix, k):
    def get_digit_sum(number):
        sum = 0
        while number > 0:
            sum += number % 10
            number /= 10
        return sum

    def check_position(row, column, k):
        if get_digit_sum(row) + get_digit_sum(column) <= k:
            return True
        return False

    moving_count = 0
    if (
            0 <= row < rows
            and 0 <= column < columns
            and not visited_matrix[row][column]
            and check_position(row, column, k)
    ):
        moving_count += 1
        visited_matrix[row][column] = True
        moving_count += moving_count_core(rows, columns, row + 1, column, visited_matrix, k) + \
                        moving_count_core(rows, columns, row - 1, column, visited_matrix, k) + \
                        moving_count_core(rows, columns, row, column + 1, visited_matrix, k) + \
                        moving_count_core(rows, columns, row, column - 1, visited_matrix, k)
    return moving_count


def moving_count(rows, columns, k):
    if rows < 1 and columns < 1 and k < 0:
        return 0
    visited_matrix = [[False for _ in range(columns)] for _ in range(rows)]
    count = moving_count_core(rows, columns, 0, 0, visited_matrix, k)
    return count


if __name__ == '__main__':
    print moving_count(3, 3, 3)
