# encoding:utf-8
"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/27 0027 下午 2:15
"""

#  Python 其实有3个方法，即静态方法（staticmethod）,类方法（classmethod）和实例方法，如下：
#  静态方法是类中的函数，不需要实例，静态方法主要用来存放逻辑性代码，主要是一些逻辑属于类，但是和类本身没有交互，即在静
#  态方法中不会涉及到类中的方法和属性的操作。可以理解为静态方法存在词类的名称空间中。事实上在python引入静态方法之前，通常是在全局名称空间中创建函数

#  例子：譬如，我想定义一个关于时间操作的类，其中有个获得当前时间的函数
import time 
class TimeTest(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())

#print(TimeTest.showTime())
#t = TimeTest(2, 10, 10)
#nowTime = t.showTime()
#print(nowTime)


# 类方法
#类方法是将类本身作为对象进行操作的方法。他和静态方法的区别在于；不管这个方式是从实例调用还是从类调用，他都用第一个参数把类传递过来
# 例子： 做一个颜色的动态匹配

class ColorTest(object):
    color = 'color'
    @classmethod
    def value(self):
        return self.color

class Red(ColorTest):
    color = 'red'

class Green(ColorTest):
    color = 'green'


#g = Green()
#print(g.value())
#print(Green.value())
#r = Red()
#print(r.value())
#print(Red.value())

# 2、假设我有一个学生类和一个班级类，想要实现的功能为：
#    班级类含有类方法：
#    执行班级人数增加的操作、获得班级的总人数
#    学生类继承自班级类，每实例化一个学生，班级人数都能增加，最后我想定义一些 学生，然后获得班级中的总人数

##   这个问题用类方法比较合适，因为我实例化的是学生，但是如果我从学生这个实例中获得班级总人数是不合理的，同时，如果想要获得班级总人数，如果生成一个班级的实例也是没有必要的


class ClassTest(object):
    print("父类")
    __num = 0
    @classmethod
    def addNum(self):
        self.__num += 1
    @classmethod
    def getNum(self):
        return self.__num

    def __new__(self):
        print('调用这里了')
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)

class Student(ClassTest):
    def __init__(self):
        self.name = ''

a = Student()
b = Student()
print(ClassTest.getNum())

