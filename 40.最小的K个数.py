# coding=utf-8
"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


class Solution(object):
    def get_least_number(self, nums, k):
        def partition(array, left, right):
            less = left - 1
            greater = right
            current = left

        start = 0
        end = len(nums) - 1
        index = partition(nums, start, end)
        while index != k - 1:
            if index > k - 1:
                start = index + 1
                index = partition(nums, start, end)
            else:
                end = index - 1
                index = partition(nums, start, end)


