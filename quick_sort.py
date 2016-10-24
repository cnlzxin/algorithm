#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cProfile
import random


def quick_sort(arr):
    """一定要分成三部分(</>/=): 1.函数递归调用少,节省时间;2.有大量重复数据时不会溢出函数栈"""

    if isinstance(arr, list):
        if len(arr) <= 1:
            return arr
        # choice()参数不能是空列表,所以先判断之后再选择基准值,顺序不能倒
        pivot = random.choice(arr)
        smaller = []
        bigger = []
        pivot_list = []
        for elem in arr:
            if elem < pivot:
                smaller.append(elem)
            elif elem > pivot:
                bigger.append(elem)
            else:
                pivot_list.append(elem)

        # 用列表生成式试一下,耗时与上面差不多,但需迭代三次,不喜欢
        # smaller = [x for x in arr if x < pivot]
        # bigger = [x for x in arr if x > pivot]
        # pivot_list = [x for x in arr if x == pivot]

        smaller = quick_sort(smaller)
        bigger = quick_sort(bigger)
        return smaller + pivot_list + bigger
    else:
        raise TypeError('type is not list')


if __name__ == '__main__':

    # 测试函数: quick_sort()
    # arr = list(range(1000))
    arr = []
    for i in range(1000):
        n = random.randint(1, 300)
        arr.append(n)
    for x in range(3):
        random.shuffle(arr)
    print('初始数据:\n', arr)
    result = quick_sort(arr)
    print('结果:\n', result)
    cProfile.run('quick_sort(arr)')
