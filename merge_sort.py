#!/usr/bin/python3
# -*- coding: utf-8 -*-


def test_merge_sort(arr):

    if isinstance(arr, list):
        length = len(arr)
        if length == 1:
            return arr
        # 拆分
        middle_index = length // 2
        left = test_merge_sort(arr[:middle_index])
        right = test_merge_sort(arr[middle_index:])

        # 开始合并
        i = 0
        j = 0
        merge_list = []
        # 提前单独写出来可以减少len()调用次数,节省时间
        length_l = len(left)
        length_r = len(right)
        while i < length_l and j < length_r:
            if left[i] < right[j]:
                merge_list.append(left[i])
                i += 1
            else:
                merge_list.append(right[j])
                j += 1
        # 合并剩余的部分
        if i < length_l:
            merge_list.extend(left[i:])
        elif j < length_r:
            merge_list.extend(right[j:])

        return merge_list
    else:
        raise TypeError('type is not list')


def test_issort(arr):
    # 判断排序是否成功
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] <= sorted_arr[i + 1]:
            continue
        else:
            print('sort fail')
            break
    if i == len(sorted_arr) - 2:
        print('sort success')

if __name__ == '__main__':

    import cProfile
    import random

    # 测试函数: test_merge_sort()
    arr = []
    for i in range(1000):
        arr.append(random.randint(1, 300))
    for x in range(3):
        random.shuffle(arr)
    sorted_arr = test_merge_sort(arr)
    cProfile.run('test_merge_sort(arr)')
    test_issort(sorted_arr)
