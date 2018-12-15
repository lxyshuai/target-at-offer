# coding=utf-8
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数：

如数组{7,5,6,4}，逆序对总共有5对，{7,5}，{7,6}，{7,4}，{5,4}，{6,4}；
"""


class Solution(object):
    def inverse_pairs(self, data):
        def merge_sort_process(array, left, right):
            if left == right:
                return
            middle = left + (right - left) / 2
            merge_sort_process(array, left, middle)
            merge_sort_process(array, middle + 1, right)
            merge(array, left, middle, right)

        def merge(array, left, middle, right):
            help = [0 for _ in range(right - left + 1)]
            help_index = right - left
            right_index = right
            left_index = middle

            while left_index >= left and right_index >= middle + 1:
                if array[right_index] < array[left_index]:
                    self.count += left_index - left + 1
                    help[help_index] = array[left_index]
                    help_index -= 1
                    left_index -= 1
                else:
                    help[help_index] = array[right_index]
                    help_index -= 1
                    right_index -= 1

            if left_index >= left:
                help[0: left_index - left + 1] = array[left:left_index + 1]
            if right_index >= middle + 1:
                help[0:right_index - middle] = array[middle + 1: right_index + 1]
            array[left:right + 1] = help

        self.count = 0
        merge_sort_process(data, 0, len(data) - 1)
        return self.count


if __name__ == '__main__':
    print Solution().inverse_pairs([7, 5, 6, 4])
