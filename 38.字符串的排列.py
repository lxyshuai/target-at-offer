# coding=utf-8
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


class Solution(object):
    def permutations(self, string):
        def process(string_list, index):
            if index == len(string_list) - 1:
                result.append(''.join(string_list))
                return
            for current_index in range(index, len(string_list)):
                string_list[index], string_list[current_index] = string_list[current_index], string_list[index]
                process(string_list, index + 1)
                string_list[index], string_list[current_index] = string_list[current_index], string_list[index]

        result = []
        process(list(string), 0)
        return result


"""
输入多个字符,求字符的所有组合
"""


class Solution(object):
    def combination(self, char_list):
        def process(before_string, index):
            if index == len(char_list):
                result.append(before_string)
                return
            process(before_string + char_list[index], index + 1)
            process(before_string, index + 1)

        result = []
        process('', 0)
        return result


"""
输入一个含有8个数字的数组，判断有没有可能把这8个数字分别放到正方体的8个顶点上，使得正方体上三组相对的面上的4个顶点的和相等
"""


class Solution(object):
    def exist(self, nums):
        def satisfy(nums):
            if sum(nums[0:4]) == sum(nums[4:8]) and \
                    nums[0] + nums[2] + nums[4] + nums[6] == nums[1] + nums[3] + nums[5] + nums[7] and \
                    nums[0] + nums[1] + nums[4] + nums[5] == nums[2] + nums[3] + nums[6] + nums[7]:
                return True
            else:
                return False

        def process(nums, index):
            if index == len(nums) - 1:
                return satisfy(nums)
            result = False
            for current_index in range(index, len(nums)):
                nums[index], nums[current_index] = nums[current_index], nums[index]
                result = result or process(nums, index + 1)
                nums[index], nums[current_index] = nums[current_index], nums[index]
            return result

        return process(nums, 0)


"""
即在8 X 8的国际象棋上摆放八个皇后，使其不能相互攻击，即任意两个皇后不得处于同一行，同一列或者同意对角线上，求出所有符合条件的摆法
"""


class Solution(object):
    def eight_queen_count(self):
        def is_queen_in_diagonal(nums):
            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if j - i == nums[j] - nums[i] or j - i == nums[i] - nums[j]:
                        return True
            return False

        def permutations(nums, index):
            if index == len(nums) - 1:
                if not is_queen_in_diagonal(nums):
                    self.count += 1
                return
            for swap_index in range(index, len(nums)):
                nums[index], nums[swap_index] = nums[swap_index], nums[index]
                permutations(nums, index + 1)
                nums[index], nums[swap_index] = nums[swap_index], nums[index]

        self.count = 0
        nums = range(8)
        permutations(nums, 0)
        return self.count


if __name__ == '__main__':
    # print Solution().permutations('abc')
    # print Solution().combination(['a', 'b', 'c'])
    # print Solution().exist(range(8))
    print Solution().eight_queen_count()