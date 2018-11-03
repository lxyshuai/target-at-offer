# coding=utf-8
"""
题目:把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如{3,4,5,1,2}为{1,2,3,4,5}
"""


def get_min(nums):
    if not nums:
        return
    left = 0
    right = len(nums) - 1
    # 如果数列没有选择,左边第一个就是最小的元素
    result = left
    # 由于是非递减数列,所以是>=
    while nums[left] >= nums[right]:
        if right - left == 1:
            result = right
            break
        middle = left + (right - left) / 2
        if nums[left] == nums[right] == nums[middle]:
            return min(nums)
        if nums[middle] >= nums[left]:
            left = middle
        elif nums[middle] <= nums[right]:
            right = middle
    return nums[result]
