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


import heapq


class Solution(object):
    def get_least_number(self, nums, k):
        heapq.heapify(nums)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(nums))
        return result


class Solution(object):
    def get_least_number(self, nums, k):
        min_heap = [float('-inf')] * k
        nums = [-number for number in nums]
        heapq.heapify(min_heap)
        for number in nums:
            if number > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, number)
        return [-number for number in min_heap]


if __name__ == '__main__':
    print Solution().get_least_number(range(100, -1, -1), 5)
