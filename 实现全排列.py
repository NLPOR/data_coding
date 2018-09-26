"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/26 0026 上午 10:57
"""
"""
递归思想：
取出数组中第一个元素放到最后，即a[1]与a[n]交换，然后递归求a[n-1]的全排列
例如：集合{1,2,3}
1、如果数组只有一个元素n = 1, a={1}则全排列就是{1}
2、如果数组元素只有两个n = 2, a={1,2}则全排列是：
{2,1}--a[1]与a[2]交换，交换后求a[2-1]={2}，归结到1、
{1,2}--a[2]与a[2]交换，交换后求a[2-1]={1}，归结到1、
3、如果数组有三个元素n=3，a={1,2,3} 则全排列是
 {{2,3},1}--a[1]与a[3]交换。后求a[3-1]={2,3}的全排列，归结到2）
 {{1,3},2)--a[2]与a[3]交换。后求a[3-1]={1,3}的全排列，归结到2）
 {{1,2},3)--a[3]与a[3]交换。后求a[3-1]={1,2}的全排列，归结到2）
 ....类推 
 
也可以按照下面的思路：
    每次循环，取出一个元素添加到结果数组中，而对剩余的元素进行相同的全排列操作，终止条件剩余的元素为1
例如：[1,2,3,4]
    全排列可以看成是将1或2或3或4(for)放在固定位置，[2,3,4]，[1,2,4],[1,3,4]的全排列。以此类推
    直到数组中仅有一个元素
"""
# COUNT = 0
#
#
# def perm(nums, begin, end):
#     global COUNT
#     if begin >= end:
#         print(nums)
#         COUNT += 1
#     else:
#         i = begin
#         for j in range(begin, end):
#             nums[j], nums[i] = nums[i], nums[j]
#             perm(nums, begin+1, end)
#             nums[j], nums[i] = nums[i], nums[j]
import copy
retsult = []
COUNT = 0
def perm_func(remian_list, res_list):
    global COUNT
    if len(remian_list) == 1:
        res_list.append(remian_list[0])
        print(res_list)
        COUNT += 1
        return res_list

    else:
        for j in range(len(remian_list)):
            remian_list_c = copy.deepcopy(remian_list)
            res_list_c = copy.deepcopy(res_list)
            twp = remian_list_c.pop(j)
            res_list_c.append(twp)
            perm_func(remian_list_c, res_list_c)


if __name__ == '__main__':
    n = [1, 2, 3, 4]
    perm_func(n, [])
    print(COUNT)

