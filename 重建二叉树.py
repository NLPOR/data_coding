"""
@author : 'XXY'
@contact : '529379497@qq.com'
@researchFie1d : 'NLP DL ML'
@date : 2018/9/24 0024 上午 9:35
"""
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树，假设输入中都不含重复的数字
实例：
前序：[1, 2, 4, 7, 3, 5, 6, 8]
中序：[4, 7, 2, 1, 5, 3, 8, 6]
输出：重构后的二叉树
'''
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def construct_tree(pre_order, mid_order):
    if len(pre_order) == 0 or len(mid_order) ==0 :
        return None
    # 前序遍历的第一个结点一定是根结点
    root_data = pre_order[0]
    for i in range(0, len(mid_order)):
        if mid_order[i] == root_data:
            break
    # 递归构造左子树和右子树
    left = construct_tree(pre_order[1:1 + i], mid_order[:i])
    right = construct_tree(pre_order[1 + i:], mid_order[i+1:])
    return Node(root_data, left, right)


if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
    root = construct_tree(pre_order, mid_order)
    print(root.data)
    print(root.left.data)
    print(root.right.data)





