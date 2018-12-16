# coding=utf-8
"""
题目一：
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度O(n)，空间复杂度O(1)。
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for number in nums:
            xor ^= number
        mask = 1
        # 找到第一个异或为1的位数
        while xor & mask == 0:
            mask = mask << 1

        result1 = 0
        result2 = 0
        for number in nums:
            if number & mask:
                result1 ^= number
            else:
                result2 ^= number
        return [result1, result2]


"""
题目二：数组中唯一只出现一次的数字
在一个数组中除一个数字只出现一次之外，其他数字都出现了三次。请找出哪个只出现一次的数字。
"""


class Solution(object):
    def singleNumber(self, nums):
        def convert(x):
            if x >= 2 ** 31:
                x -= 2 ** 32
            return x

        result = 0
        for i in xrange(32):
            count = 0
            for number in nums:
                count += (number >> i) & 1
            result |= (count % 3) << i
        return convert(result)


class Solution(object):
    def singleNumber(self, nums):
        def convert(x):
            if x >= 2 ** 31:
                x -= 2 ** 32
            return x

        result = 0
        bin_result = [0 for _ in range(32)]
        for number in nums:
            for index in range(32):
                bin_result[index] += (number >> index) & 1
        for index, count in enumerate(bin_result):
            result |= (count % 3) << index
        return convert(result)
