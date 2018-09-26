"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/11 0011 下午 3:04
"""
from collections import deque

'''
    堆排序是指利用堆这种数据结构所设计的一种选择排序算法：
    1. 由输入的无序数组构造一个最大堆，作为初始的无序区
    2. 把堆顶元素（最大值）和堆尾元素互换
    3. 把堆（无序区）的尺寸缩小1，并调用heapify()从新的堆顶元素进行堆调整
    4. 重复步骤2，直到堆的尺寸为1
'''


def swap_param(L, i, j):
    #  交换数组中的两个值
    L[i], L[j] = L[j], L[i]
    return L


def heap_adjust(L, start, end):
    # 将L调整为堆
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    for i in range(first_sort_count):
        # 把序列调整为一个大根堆
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        # 把堆顶元素和堆尾元素交换，然后把剩下的元素调整为一个大根堆
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


def main():
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))


if __name__ == '__main__':
    main()

