"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/24 0024 上午 11:15
"""

'''
把一个数组最开始的若干个元素搬到素组的末尾，称之为数组的旋转。输入一个递增排序的数组的一个旋转
输出旋转数组的最小值
输入：{3,4,5,1,2}
输出：1
'''


def min_number_rotate_array(rotate_array):
    p1 = 0
    p2 = len(rotate_array) - 1
    mid = p1
    while rotate_array[p1] >= rotate_array[p2]:
        if p2 - p1 == 1:
            mid = p2
            break
        mid = (p1+p2) // 2
        if rotate_array[mid] >= rotate_array[p2]:
            p1 = mid
        elif rotate_array[mid] <= rotate_array[p2]:
            p2 = mid
    return rotate_array[mid]


print(min_number_rotate_array([4, 5, 6, 7, 2, 3]))

