"""
@author = 'XXY'
@contact = '529379497@qq.com'
@researchFie1d = 'NLP DL ML'
@date= '2017/12/21 10:18'
"""


'''
 总共n个学生，从中选k个学生计算乘积
      ==============================
      f(k, i)表示选出的第k个学生编号为i的能力值
      f(k, i) = MAX(f(k-1, i-1),f(k-1, i-2),....f(k-1, i-d)) * 第i个学生的能力  或者
      f(k, i) = MIN(f(k-1, i-1),f(k-1, i-2),....f(k-1, i-d)) * 第i个学生的能力 （因为可能为负值）
      ==============================
    f(i,k)代表选出k个学生，最后一个学生编号是i.. i从0到n-1
    最终在f(0,k),f(1,k),f(2,k)...f(n-1,k)中选取最大的乘积作为结果
    
    所以现在要解决的问题是怎么求f(i,k)
    假设第k-1个学生的编号为j,f(j,k-1)已知
    那么f(i,k)就可以用到f(j,k-1)的条件了。但由于学生的能力值可以为负数。
    若第i个学生的能力值为负数，要使乘积最大，则应求f(j,k-1)的最小值，记为Min.f(j,k-1)；
    若第i个学生的能力值为正数，要使乘积最大，则应求f(j,k-1)的最大值，记为Max.f(j,k-1)。
    因此应该设立两个数组同时保存选取第k-1个学生后乘积的最大和最小值。
    
    values(i)代表第i个学生的能力值
    状态方程为：f(i,k) = max(f(i,k), Min.f(j,k-1)*values(i), Max.f(j,k-1)*values(i))
    
    由于i和j满足条件 i-j <= d,所以在满足条件的j中选取最大的值作为f(i,k)的值
'''
n = int(input('请输入学生个数n: '))
arr = [int(x) for x in input('请输入每个学生的能力值arr: ').split()]   # 每个学生的能力值
K, D = [int(x) for x in input('请输入要选取的学生个数K和编号间隔D: ').split()]  # 从K个学生中选D个
fm = [([0] * n) for i in range(K)]  # k*d
fn = [([0] * n) for i in range(K)]  # k*d
res = 0                             # 保存乘积最大值

for i in range(n):
    fm[0][i] = arr[i]
    fn[0][i] = arr[i]

for i in range(n):
    # 第一层循环，遍历每一个学生，从每一个学生开始选取，选择k个学生出来，计算乘积保存在res中
    for k in range(1, K):
        # 第二层循环，选出K个学生
        # for j in range(i-1,-1,-1):
        for j in range(i - 1, max(0, i - D) - 1, -1):
            # if (i-j<D and k>0):
            # 第三层循环，从编号为i-D到i之间的学生中找到能力值最大最小的那个学生
            fm[k][i] = max(fm[k][i], max(fm[k - 1][j] * arr[i], fn[k - 1][j] * arr[i]))
            fn[k][i] = min(fn[k][i], min(fm[k - 1][j] * arr[i], fn[k - 1][j] * arr[i]))
            # fm[k][i] = max(fm[0][i],max(fm[k-1][j]*arr[i], fn[k-1][j]*arr[i]))
            # fn[k][i] = min(fn[0][i],min(fm[k-1][j]*arr[i], fn[k-1][j]*arr[i]))
            # fm[k][i] = max(fm[k-1][j]*arr[i], fn[k-1][j]*arr[i])
            # fn[k][i] = min(fm[k-1][j]*arr[i], fn[k-1][j]*arr[i])
    res = max(res, fm[K - 1][i])    # 从res中选择最大的即为最后的输出
print(res)