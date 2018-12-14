# coding=utf-8
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""
"""
用一个大根堆和一个小根堆
大根堆存储前n/2个数,小根堆存储后n/2个数
每出入一个数,可能要调整大根堆和小根堆的数量,保持差距数量在1以内
"""
import heapq


class MedianHolder(object):
    def __init__(self):
        self.max_heap = list()
        self.min_heap = list()

    def modify_two_heaps_size(self):
        if len(self.max_heap) >= len(self.min_heap) + 2:
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        elif len(self.min_heap) >= len(self.max_heap) + 2:
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def add_number(self, number):
        """
        大于大根堆堆顶放入小根堆
        @param number:
        @type number:
        @return:
        @rtype:
        """
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -1 * number)
        else:
            if number > -1 * self.max_heap[0]:
                heapq.heappush(self.min_heap, number)
            else:
                heapq.heappush(self.max_heap, -1 * number)
        self.modify_two_heaps_size()

    def get_median(self):
        max_heap_size = len(self.max_heap)
        min_heap_size = len(self.min_heap)
        total_size = max_heap_size + min_heap_size
        max_heap_root = -1 * self.max_heap[0]
        min_heap_root = self.min_heap[0]
        if total_size == 0:
            return
        elif total_size % 2 == 0:
            return (max_heap_root + min_heap_root) / 2
        else:
            return max_heap_root if max_heap_size > min_heap_size else min_heap_root


if __name__ == '__main__':
    md = MedianHolder()
    md.add_number(1)
    md.add_number(2)
    print md.get_median()
    md.add_number(3)
    print md.get_median()
    md.add_number(4)
    md.add_number(5)
    print md.get_median()
