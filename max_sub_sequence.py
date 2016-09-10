#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
# 问题: 给定整书A1，A2，……，AN（可能有负数），设整数k取值i到j(i<=j),求Ai到Aj的和的最大值（所有整数均为负数，则最大子序列和为0）
# 例如： 输入-2，11，-4，13，-5，-2时，答案为20（从A2到A4）
"""


def max_subsequence_sum(arr):

    max_sum = 0
    sub_sum = 0

    for elem in arr:
        sub_sum += elem

        if sub_sum > max_sum:
            max_sum = sub_sum
        elif sub_sum < 0:
            sub_sum = 0

    return max_sum


def generate_random_list(n, x, y):
    """
    # n: 元素个数
    # x: 取值下限
    # y: 取值上限
    # 返回一个无序随机数组 arr
    """
    import random

    arr = []
    for i in range(n):
        n = random.randint(x, y)
        arr.append(n)
    for x in range(3):
        random.shuffle(arr)
    return arr

if __name__ == '__main__':
    import cProfile

    arr = generate_random_list(1000, -100, 300)
    print(arr)
    # arr = [-2, 11, -4, 13, -5, -2]
    sub_arr = max_subsequence_sum(arr)
    print(sub_arr)
    cProfile.run('max_subsequence_sum(arr)')
