"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/26 0026 下午 3:16
"""
""""
解决八皇后问题可以分为两个层面：
1、找出第一种正确摆放方式，也就是深度优先遍历
2、找出全部的正确摆放方式，也就是广度优先遍历

代码实现需要解决以下几个问题：
1、国际象棋的期盼如何表示？
    用一个长度是8的二维数组表示即可
2、如何判断皇后落点是否规范
    定义一个conflict方法，传入新皇后的落点，通过纵向和斜向是否存在其他皇后来判断是否合规
3、如何递归回溯
    递归回溯是算法的核心，代码逻辑有些复杂
4、如何输出结果
    直接遍历二维数组并输出即可
5、如何串起来？
    在main函数里分三步来调用
    第一步：初始化
    第二步：递归摆放皇后
    第三步：最后输出结果
"""
import random
import sys

sys.setrecursionlimit(10000000)
# 例如这里设置为一百万执行：fact(1000)，能正确出结果了。但是，好像只可以执行到  fact(3930) 左右。

def conflict(state, nextX):
    # 冲突检查，采用state来表示每个皇后的位置，其中索引用来表示横坐标，其对应的值表示纵坐标。例如：state[0] = 3，表示该皇后位于第一行的第四列
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下左右），或在同一对角线上，则说明有冲突，需要重新摆放
        if abs(state[i] - nextX) in (0, nextY - i):
            # 如果下一个皇后和正在考虑的前一个皇后的水平距离为0或者垂直距离相等，就返回True否则返回False
            return True
        return False


# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置
def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 产生当前皇后的位置信息
            # 如果只剩下一个皇后没有放置
            if len(state) == 1:
                yield (pos,)
            # 否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            # 程序要从前面的皇后得到包含位置信息的元组（元组不可更改）
            # 并要为后面的皇后提供当前皇后的每一种合法的位置信息
            # 所以把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
    else:
        for result in queens(num, state + (pos,)):
            yield (pos,) + result


# 为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
    for pos in solution:
        print(line(pos))
        for item in queens(8):
            print(item)


if __name__ == "__main__":
    prettyprint(random.choice(list(queens(8))))