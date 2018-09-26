"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/11 0011 上午 9:35
"""
def bubble_srot(li):
    '''
    冒泡排序:
    1.比较相邻的元素，如果前一个比后一个大，就把它们调换位置
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这一步结束后最后的元素是最大的
    3.针对所有的元素重复以上的步骤，除了最后一个
    4.持续每次对越来越少的元素重复上面的步骤，知道没有任何一对数字需要比较
    性能：
    时间复杂度： O(n^2)
    空间复杂度： O(1)
    稳定性：     稳定

    :param li:
    :return:
    '''
    for i in range(len(li) - 1):
        for j in range(len(li) - i -1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def cocktail_sort(li):
    """
    鸡尾酒排序：
    与冒泡排序的不同之处在于从低到高然后从高到低，而冒泡排序则仅从低到高去比较序列里的元素
    :param li:
    :return:
    """
    start = 0
    end = len(li) - 1
    while start < end:
        for i in range(start, end):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
        end -= 1
        for j in range(end, start, -1):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
        start += 1
    return li



def select_sort(li):
    '''
    选择排序：
    初始时在序列中找到最小（大）的元素，放到序列的起始位置作为已拍序列；然后，再从剩余未排序元
    素中继续寻找最小（大）元素，放到已排序序列的末尾。一次类推，知道所有元素均排序完毕
    性能：
    时间复杂度： O(n^2)
    空间复杂度： O(1)
    稳定性：     不稳定
    :param li:
    :return:
    '''
    for i in range(len(li) - 1):
        min = i     # 选择一个最小的
        for j in range(i+1, len(li)):
            if li[min] > li[j]:
                li[min], li[j] = li[j], li[min]
    return li


def insert_sort(li):
    '''
    插入排序：
    1.从第一个元素开始，该元素可以认为已经呗排序
    2.取出下一个元素，在已经排序的元素序列中从后向前扫描
    3.如果该元素（已排序）大于新元素，将该元素一道下一位置
    4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5.将新元素插入到该位置
    6.重复步骤2-5
    时间复杂度： O(n^2)
    空间复杂度： O(1)
    稳定性：     不稳定
    :param li:
    :return:
    '''
    for i in range(len(li) - 1):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            # 将当前数值与左边已排序的数组进行比较并插入到相应的位置
            li[j+1] = li[j]
            j = j - 1
            li[j + 1] = tmp
    return li


def quick_sort(li, start, end):
    '''
    快速排序：
    1.从序列中挑出一个元素，作为基准
    2.把所有比基准值晓得元素放在基准前面，所有比基准值大的元素放在基准的后面（相同的数可以放大任一边），
      这个分区成为partition操作
    3.对每个分区递归的进行步骤1-2，递归结束条件是序列的大小是0或者1，这时候整体已经呗排好序了
    性能：
    时间复杂度：O(nlogn)
    空间复杂度：O(nlogn)
    稳定性：不稳定
    :param li:    待排序数组
    :param start: 数组起始位置
    :param end:   数组结束位置
    :return:      返回枢纽位置
    '''
    def partition(li, start, end):
        left = start
        right = end
        # 将最左侧的值赋值给参考值k
        k = li[start]
        # 当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
        while left < right:
            # 当left对应的值小于k参考值，就一直向右移动
            while li[left] <= k:
                left += 1
            # 当right对应的值大于k参考值，就一直向左移动
            while li[right] > k:
                right = right - 1
            # 若移动完，二者仍未相遇则交换下标对应的值
            if left < right:
                li[left], li[right] = li[right], li[left]
        # 若移动完，已经相遇，则交换right对应的值和参考值
        li[start] = li[right]
        li[right] = k
        # 返回k值
        return right
    if start < end:
        div_index = partition(li, start, end)
        quick_sort(li, start, div_index)
        quick_sort(li, div_index + 1, end)
    else:
        return



if __name__ == '__main__':
    li = [345, 456, 68, 435, 1, 6, 4, 568]
    print("冒泡排序：", bubble_srot(li))
    li = [345, 456, 68, 435, 1, 6, 4, 568]
    print("鸡尾酒排序：", cocktail_sort(li))
    li = [345, 456, 68, 435, 1, 6, 4, 568]
    print("选择排序：", select_sort(li))
    li = [345, 456, 68, 435, 1, 6, 4, 568]
    print("插入排序：", select_sort(li))
    li = [345, 456, 68, 435, 1, 6, 4, 568]
    print('排序前：', li)
    quick_sort(li, 0, len(li) - 1)
    print('快速排序：', li)
