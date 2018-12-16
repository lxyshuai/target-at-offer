# coding=utf-8
"""
题目一：滑动窗口的最大值
"""
import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []

        result = []
        deque = collections.deque()

        # 首先将前k个数加入deq
        for index in range(k):
            while len(deque) != 0:
                if nums[index] > nums[deque[-1]]:
                    deque.pop()
                else:
                    break
            deque.append(index)

        # 开始记录result
        for index in range(k + 1, len(nums)):
            result.append(nums[deque[-1]])

            # 如果最大值小标超出窗口范围，弹出
            if deque[0] < index - k + 1:
                deque.pop()
            while len(deque) != 0:
                if nums[index] > nums[deque[-1]]:
                    deque.pop()
                else:
                    break
            deque.append(index)

        result.append(nums[deque[0]])

        return result


"""
题目二：队列的最大值
定义一个队列并实现函数max得到队列里的最大值，要去函数max,push_back,pop_front的时间复杂度O(1)
"""


class InternalData(object):
    def __init__(self, index, value):
        self.index = index
        self.value = value


class QueueWithMax(object):
    def __init__(self):
        self.queue = collections.deque()
        self.max_queue = collections.deque()
        self.current_index = 0

    def append(self, value):
        while len(self.queue) != 0:
            if value >= self.max_queue[-1].value:
                self.max_queue.pop()

        internal_data = InternalData(self.current_index, value)
        self.queue.append(internal_data)
        self.max_queue.append(internal_data)
        self.current_index += 1

    def pop_front(self):
        if len(self.max_queue) == 0:
            raise Exception

        if self.max_queue[0].index == self.queue[0].index:
            self.max_queue.popleft()
        self.queue.popleft()

    def max(self):
        if len(self.max_queue) == 0:
            raise Exception

        return self.max_queue[0].value
