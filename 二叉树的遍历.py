"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/24 0024 上午 11:08
"""
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_traverse(root):
    """
    前序遍历
    :param root:
    :return:
    """
    if root == None:
        return
    print(root.value)
    pre_traverse(root.left)
    pre_traverse(root.right)


def mid_traverse(root):
    """
    中序遍历
    :param root:
    :return:
    """
    if root == None:
        return
    mid_traverse(root.left)
    print(root.value)
    mid_traverse(root.right)

def after_traverse(root):
    """
    中序遍历
    :param root:
    :return:
    """
    if root == None:
        return
    mid_traverse(root.left)
    mid_traverse(root.right)
    print(root.value)

if __name__=='__main__':
    root=Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    print('前序遍历：')
    pre_traverse(root)
    print('\n')
    print('中序遍历：')
    mid_traverse(root)
    print('\n')
    print('后序遍历：')
    after_traverse(root)
    print('\n')