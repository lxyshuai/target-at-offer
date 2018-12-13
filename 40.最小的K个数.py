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
            while current < greater:
                if array[current] < array[right]:
                    less += 1
                    array[current], array[less] = array[less], array[current]
                    current += 1
                elif array[current] > array[right]:
                    greater -= 1
                    array[current], array[greater] = array[greater], array[current]
                else:
                    current += 1
            array[greater], array[right] = array[right], array[greater]
            greater += 1
            return greater - 1

        start = 0
        end = len(nums) - 1
        index = partition(nums, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = partition(nums, start, end)
            else:
                start = index + 1
                index = partition(nums, start, end)
        return nums[:k]


if __name__ == '__main__':
    print Solution().get_least_number(range(100, -1, -1), 5)
