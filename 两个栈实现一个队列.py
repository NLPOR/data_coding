"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/23 0023 上午 11:10
"""
'''
两个栈(A,B)实现一个队列
入队：元素进栈A
出队：先判断栈B是否为空，为空则将栈A中的元素 pop 出来并 push 进栈B，再栈B出栈，如不为空则栈B直接出栈
复杂度分析：
这样用两个栈实现一个队列,入队的复杂度为O(1)，出队的复杂度则变为O(n)。
而直接用 python 的单个列表实现队列，以列表首作为队列尾，则入队用insert，复杂度为O(n)，出队用pop，复杂度为O(1)。（列表首，即列表中下标为0的元素）
实现：就以列表作为栈的底层实现，只要保证后进先出的约束就是栈。这里只实现入队和出队两个操作。
'''
class Queue:
    def __init__(self):
        self.stockA = []
        self.stockB = []

    def push(self, node):   # 入栈操作
        self.stockA.append(node)

    def out(self):
        if self.stockB == []:       # 如果栈B为空
            if self.stockA == []:   # 如果栈A为空
                return None
            else:                   # 如果栈A不为空
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()

if __name__=='__main__':
    times = 5
    testList = list(range(times))
    testQueue = Queue()
    for i in range(times):
        testQueue.push(testList[i])
    print(testList)
    for i in range(times):
        print(testQueue.out(), ',', end='')   #end=''可以让 print 输出不换行

