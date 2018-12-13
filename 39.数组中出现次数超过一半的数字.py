# coding=utf-8
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution(object):
    def more_than_half_num(self, nums):
        def partition(array, left, right):
            less = left - 1
            greater = right
            current = left
            while current < greater:
                if array[current] < array[right]:
                    less += 1
                    array[less], array[current] = array[current], array[less]
                    current += 1
                elif array[current] > array[right]:
                    greater -= 1
                    array[greater], array[current] = array[current], array[greater]
                else:
                    current += 1
            array[greater], array[right] = array[right], array[greater]
            greater += 1
            return greater - 1

        middle_index = len(nums) / 2
        start = 0
        end = len(nums) - 1
        index = partition(nums, start, end)

        while index != middle_index:
            if index > middle_index:
                end = index - 1
                index = partition(nums, start, end)
            else:
                start = index + 1
                index = partition(nums, start, end)

        return nums[index]


class Solution(object):
    def more_than_half_num(self, nums):
        count = 0
        result = None
        for current_index, current_number in enumerate(nums):
            if count == 0:
                result = current_number
                count += 1
            else:
                if current_number != nums[current_index - 1]:
                    count -= 1
                else:
                    count += 1
        return result


if __name__ == '__main__':
    print Solution().more_than_half_num([1, 2, 2, 3, 2])
