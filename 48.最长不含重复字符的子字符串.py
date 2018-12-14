# coding=utf-8
"""
最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含从’a’到’z’的字符。例如，在字符串中”arabcacfr”，最长非重复子字符串为”acfr”，长度为4。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_appear_dict = {}
        max_length = 0
        left = -1
        for index, char in enumerate(s):
            if char in last_appear_dict and left < last_appear_dict[char]:
                left = last_appear_dict[char]
            last_appear_dict[char] = index
            max_length = max(max_length, index - left)
        return max_length


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("tmmzuxt")
