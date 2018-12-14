# coding=utf-8
"""
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，知道到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿多少价值的礼物？
"""


class Solution(object):
    def get_max_value(self, matrix):
        def process(before_sum, row, column):

            if row == rows - 1 and column == columns - 1:
                self.max_value = max(self.max_value, before_sum + matrix[row][column])
                return
            if row >= rows:
                return
            if column >= columns:
                return
            process(before_sum + matrix[row][column], row + 1, column)
            process(before_sum + matrix[row][column], row, column + 1)

        self.max_value = float('-inf')
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        process(0, 0, 0)
        return self.max_value


class Solution(object):
    def get_max_value(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        dp = [[0 for _ in range(columns)] for _ in range(rows)]
        dp[rows - 1][columns - 1] = matrix[rows - 1][columns - 1]

        for row in range(rows - 2, -1, -1):
            dp[row][columns - 1] = dp[row + 1][columns - 1] + matrix[row][columns - 1]
        for column in range(columns - 2, -1, -1):
            dp[rows - 1][column] = dp[rows - 1][column + 1] + matrix[rows - 1][column]

        for row in range(rows - 2, -1, -1):
            for column in range(columns - 2, -1, -1):
                dp[row][column] = max(dp[row + 1][column], dp[row][column + 1]) + matrix[row][column]
        return dp[0][0]


if __name__ == '__main__':
    print Solution().get_max_value([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]
                                    ])
