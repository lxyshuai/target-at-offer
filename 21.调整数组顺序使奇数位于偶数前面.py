# coding=utf-8
"""
题目:
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
"""


def is_even(number):
    if number & 1 == 0:
        return True
    return False


def record_odd_even(nums, func):
    # 如果数组为空
    if not nums:
        return nums
    # 如果数组只有一个数字
    if len(nums) == 1:
        return nums
    begin = 0
    end = len(nums) - 1
    while begin < end:
        # 找偶数,但是不要找过头了
        while begin < end and not func(nums[begin]):
            begin += 1
        # 找奇数，但是不要找过头了
        while begin < end and func(nums[end]):
            end -= 1

        if begin != end:
            nums[begin], nums[end] = nums[end], nums[begin]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 0]
    record_odd_even(nums, is_even)
    print nums
