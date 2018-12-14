# coding=utf-8
"""
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，知道到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿多少价值的礼物？
"""
class Solution(object):
    def get_max_value(self, matrix):
        def process(row, column):
