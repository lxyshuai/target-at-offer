# coding=utf-8
"""
题目一：和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的数组的和等于s，输出任意一对
"""


class Solution(object):
    def find_numbers_with_sum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                return [nums[left], nums[right]]
            elif two_sum > target:
                right = right - 1
            else:
                left = left + 1
        return []


"""
题目二：和为s的连续正数序列
"""


class Solution(object):
    def find_continuous_sequence(self, target):
        if target < 3:
            return
        begin = 1
        end = 2
        middle = (1 + target) / 2
        current_sum = begin + end
        result = []
        while begin < middle:
            if current_sum == target:
                result.append([begin, end])
                end += 1
                current_sum += end
            elif current_sum < target:
                while end > begin and current_sum < target:
                    end += 1
                    current_sum += end
            elif current_sum > target:
                while begin < middle and current_sum > target:
                    current_sum -= begin
                    begin += 1
        return result


print Solution().find_continuous_sequence(15)
