"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/25 0025 下午 6:54
"""

"""
思路：对输入的两个字符串分别建立hash表（用字典{key:value}实现）需要从a-z,A-Z，遍历一次字符串，每出现一个字符对应的key值加1。之后比较连个hash表，
判断是否某个字符在两个hash表中都存在，如果是就用‘_’替换。最后输出字符串。
"""


def replace_same(str1, str2):
    l1 = list(str1)
    l2 = list(str2)
    hashTable1 = {}
    hashTable2 = {}
    for i in range(65, 91):
        hashTable1[i] = 0
        hashTable2[i] = 0
    for i in range(97, 123):
        hashTable1[i] = 0
        hashTable2[i] = 0
    for i in l1:
        hashTable1[ord(i)] += 1
    for i in l2:
        hashTable2[ord(i)] += 1
    for i in l1 if len(l1)>=len(l2) else l2:
        if hashTable1[ord(i)]>0 and hashTable2[ord(i)]>0:
            l1[l1.index(i)] = '_'
            l2[l2.index(i)] = '_'
    print("".join(l1))
    print("".join(l2))
def judge(str1, str2):
    if len(str1) > 10 or len(str2)>10:
        print('请输入长度不超过100的字符串')
        return False
    elif str1=="" or str2=="":
        print('字符串不能为空')
        return False
    for j in a:
        if 65<=ord(j)<=90 or 97<=ord(j)<=122:
            continue
        else:
            print('请输入只包含字母的字符串')
            return False
    return True
if __name__ == '__main__':
    a = input("a=")
    b = input("b=")
    if judge(a, b):
        replaceSame(a, b)