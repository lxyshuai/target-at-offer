# coding=utf-8
"""
题目要求：
给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”...25翻译成“z”。一个数字有多种翻译可能，例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""


class Solution(object):
    def get_translation_count(self, number):
        def combination(index):
            if index == len(number_list):
                self.count += 1
                return
            if index < len(number_list) - 1 and 10 <= number_list[index] * 10 + number_list[index + 1] <= 25:
                combination(index + 2)
            combination(index + 1)

        self.count = 0
        number_list = map(int, list(str(number)))
        combination(0)
        return self.count


class Solution(object):
    def get_translation_count(self, number):
        number_list = map(int, list(str(number)))
        dp = [0 for _ in range(len(number_list) + 1)]
        dp[-2] = 1
        for index in range(len(number_list) - 2, -1, -1):
            if 10 <= number_list[index] * 10 + number_list[index + 1] <= 25:
                dp[index] = dp[index + 1] + dp[index + 2]
            else:
                dp[index] = dp[index + 1]
        return dp[0]


if __name__ == '__main__':
    print Solution().get_translation_count(12258)
