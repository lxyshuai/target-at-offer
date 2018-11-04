# coding=utf-8
"""
题目:
给定一长为n的绳子，要求把绳子剪成m段（m，n都是整数且n>1，m>1）,每段绳子的长度记为ｋ[0], k[1], k[2]…,k[m]。
请问k[0]*k[1]*k[2]….*k[m]可能的最大乘积是多少？例如，当绳子的长度是８时，可以剪成２＊３＊３的三段得到最大的乘积。
数学证明：对与长度为n的绳子，当其剪为长度为k和n-k的两段绳子时，其乘积为k(n−k)k(n−k)，通过求导可以发现当k接近n/2时，其乘积最大。
以此推及到n=4和n=5的情况（n<4的情况上述已经计算）。当n=4，则k=2时取得最大乘积；当n=5，则k=3时取得最大乘积。此时乘积为3(n−3)3(n−3)。
因此当n>=5n>=5时，应该尽可能多地剪出长度为3的绳子段。（任何比5大的整数切分成两段的结果最终都会归结到绳子段长为3,4,5的情况）

"""
import sys


def max_product_after_cutting_recursive(length):
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    return process(length)


def process(length):
    if length == 1:
        return 1
    if length == 2:
        return 2
    if length == 3:
        return 3

    max_product = -sys.maxint
    for i in range(1, length):
        max_product = max(max_product, process(i) *
                          process(length - i))
    return max_product


def max_product_after_cutting_dp(length):
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    dp = [-sys.maxint for _ in range(length + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for index in range(length + 1):
        for diff in range(1, index / 2 + 1):
            dp[index] = max(dp[index], dp[diff] * dp[index - diff])
    return dp[length]


def max_product_after_cutting_greedy(length):
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    time_of_three = length / 3
    if length - time_of_three * 3 == 1:
        time_of_three -= 1
    time_of_two = length - time_of_three * 3 / 2
    return pow(time_of_two, 2) * pow(time_of_three, 3)


if __name__ == '__main__':
    print max_product_after_cutting_greedy(999999)
    print max_product_after_cutting_recursive(999999)