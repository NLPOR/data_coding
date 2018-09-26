"""
@author = 'XXY'
@contact = '529379497@qq.com'
@researchFie1d = 'NLP DL ML'
@date= '2018/18/28 10:30'
"""
'''
题目描述
给定一个已排序的整数组 A，和一个待查找的目标值整数target。 数组 A下标从 0开始，元素可能有重复。要求返回数组中与开始，
元素可能有重复。要求返回数组中与target值相等或最近的元素下标。任何异常情况，返回 -1。要求复杂度为O(logn)
例如 ：
A=[1,2,3]，target=2，输出 [1]
A=[1,4,6]，target=3，输出 [1]
A=[1,4,6]，target=5，输出 [1,2]
A=[1,3,3,4]，target=2，输出 ，输出 [0,1,2]


解题思路：该题目是数组查找的一种变形，由于所给数组有序而且时间复杂度要求为O(logn),所以我们考虑使用二分发进行
          查找(时间复杂度为O(logn))，来找到最佳位置。可分为两种情况
          第一种情况：如果二分法查找能够直接找到目标值可能有多个接返回目标值索引
          第二种情况：如果没有找到那么返回数组中该插入的位置索引即中位数mid，并且根据目标值的情况向左右两边查找
                      0 < mid < n:说明找到了或者没有找到，如果没有找到，则从mid往左右两边找，找出符合条件的所有数
                      mid == 0：说明目标值比目标数组都要小，只向右查找，计算距离最小的值
                      mid == n: 说明目标值比目标数组都要大，只向左查找，计算距离最小的值
'''


def bi_search(A, target):
    '''
    :param A: 给定有序数组
    :param target:  查找目标值
    :return:  返回查找结果的索引或者是目前最佳位置
    '''
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def main(A, target):
    n = len(A)
    if n == 0:
        return -1
    mid = bi_search(A, target)
    index = []          # 返回符合条件的索引值
    i, j = -1, n        # 待定的索引值
    left, right = 0, 0  # 向左向右查找的位置
    if 0 < mid < n:     # 如果找到了
        i, j = mid - 1, mid
        temp = min(abs(A[i] - target), abs(A[j] - target))
        left, right = 1, 1
    elif mid == 0:      # 小于数组中的所有值
        j = mid
        temp = abs(A[j] - target)
        left, right = 0, 1
    elif mid == n:      # 大于数组中的所有值
        i = mid - 1
        temp = abs(A[i] - target)
        left, right = 1, 0

    while left == 1 or right == 1:  # 开始向两边查找
        if i == -1:
            left = 0
        if j == n:
            right = 0
        if left == 1 and i >= 0:
            l = abs(A[i] - target)
            if l == temp:
                index = [i] + index
                i -= 1
            else:
                left = 0
        if right == 1 and j < len(A):
            r = abs(A[j] - target)
            if temp == r:
                index = index + [j]
                j += 1
            else:
                right = 0
    return index



###### 测试案例 ######
nums, target = [], 2
nums1, target1 = [1, 2, 3], 2
nums2, target2 = [1, 4, 6], 3
nums3, target3 = [1, 4, 6], 5
nums4, target4 = [1, 3, 3, 4], 2

print(main(nums, target))
print(main(nums1, target1))
print(main(nums2, target2))
print(main(nums3, target3))
print(main(nums4, target4))
