#!/usr/bin/python3
# -*- coding: utf-8 -*-


def test_bubble_sort(arr):
    """和快排不是一个档次的, bubble vs quick: 0.077s vs 0.006s"""

    if isinstance(arr, list):
        length = len(arr)
        if length <= 1:
            return arr
        for cycles in range(length - 1):            # 循环次数
            for i in range(length - cycles - 1):    # 比较范围
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr
    else:
        raise TypeError('not list')

if __name__ == '__main__':

    import cProfile
    import random

    # 测试函数: test_bubble_sort()
    arr = []
    for i in range(1000):
        n = random.randint(1, 300)
        arr.append(n)
    for x in range(3):
        random.shuffle(arr)
    print(arr)
    sorted_arr = test_bubble_sort(arr)
    print(sorted_arr)
    cProfile.run('test_bubble_sort(arr)')
