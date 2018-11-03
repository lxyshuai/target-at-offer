# coding=utf-8
"""
题目一:找出数组重复的数字
在一个长度为n的数组里的所有数字都在1到n-1的范围内。 有一个数字重复若干次，找出这个数字。
"""


def duplicate(nums):
    if not nums:
        return False
    for index in range(len(nums)):
        while index != nums[index]:
            if nums[nums[index]] == nums[index]:
                return nums[index]
            nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
    return False


"""
题目二:不修改数组找出重复的数字
不修改数组找出重复的数字。在一个长度为n+1的数组中的所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的。
在不修改输入数组的情况下找出数组中任意一个重复数字。例如输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，则对应输出的是2或者3。
"""


def get_duplication(nums):
    start = 1
    end = len(nums) - 1
    while start < end:
        middle = start + (end - start) / 2
        number_count = count(nums, start, middle)
        if number_count > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    if number_count > 1:
        return start


def count(nums, start, end):
    if not nums:
        return 0
    count = 0
    for number in nums:
        if end >= number >= start:
            count += 1
    return count


if __name__ == '__main__':
    print duplicate([2, 3, 1, 0, 2, 5, 3])
    print get_duplication([2, 3, 5, 4, 3, 2, 6, 7])
