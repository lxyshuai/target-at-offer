# coding=utf-8
"""
题目1：
统计一个数字在排序数组中出现的次数。
"""


class Solution(object):
    def get_count_of_number(self, nums, number):
        def get_first_of_number(nums, number):
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = left + (right - left) / 2
                if nums[middle] >= number:
                    right = middle - 1
                else:
                    left = middle + 1
            return right + 1

        def get_last_of_number(nums, number):
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = left + (right - left) / 2
                if nums[middle] > number:
                    right = middle - 1
                else:
                    left = middle + 1
            return right

        return get_last_of_number(nums, number) - get_first_of_number(nums, number) + 1


"""
题目二：0~n-1中缺少的数字
"""


class Solution(object):
    def get_missing_number(self, nums):
        diff = (0 + len(nums) - 1) * len(nums) / 2 - sum(nums)
        return None if diff == 0 else diff


class Solution(object):
    def get_missing_number(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] == middle:
                left = middle + 1
            elif nums[middle] != middle:
                if middle == 0 or nums[middle - 1] == middle - 1:
                    return middle
                else:
                    right = middle - 1


"""
数组中数值和下标相等的元素
"""


class Solution(object):
    def get_number_same_as_index(self, nums):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] > middle:
                right = middle - 1
            elif nums[middle] < middle:
                left = left + 1
            else:
                return middle
        return -1


if __name__ == '__main__':
    # print Solution().get_count_of_number([1, 2, 3, 3, 3, 3, 4, 4], 3)
    # print Solution().get_missing_number([0, 1, 2])
    print Solution().get_number_same_as_index([-3, -1, 1, 3, 5])
