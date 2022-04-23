# coding: utf-8
#
# rbnode.py : 赤黒木用操作関数 (2-3-4 木をベース)
#
#             Copyright (C) 2008 Makoto Hiroi
#

# 終端
null = None

# 色
BLACK = 0
RED = 1

# 節
class Node:
    def __init__(self, x, color = RED):
        self.data = x
        self.color = color
        self.left = null
        self.right = null

# 終端の設定
def make_null():
    global null
    if null is None:
        null = Node(None, BLACK)
        null.left = None
        null.right = None
    return null

# 右回転
def rotate_right(node):
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    lnode.color = node.color
    node.color = RED
    return lnode

# 左回転
def rotate_left(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    rnode.color = node.color
    node.color = RED
    return rnode

#
# データの探索
#
def search(node, x):
    while node is not null:
        if x == node.data: return True
        elif x < node.data:
            node = node.left
        else:
            node = node.right
    return False

#
# データの挿入
#

# 4node の分割
def split(node):
    node.color = RED
    node.left.color = BLACK
    node.right.color = BLACK

# 左部分木の修正
def balance_insert_left(node, flag):
    if flag: return node, flag
    if node.color == BLACK:
        flag = True
        # 左(赤)の子に赤があるか
        if node.left.right.color == RED:
            node.left = rotate_left(node.left)
        if node.left.left.color == RED:
            # 赤が 2 つ続く
            if node.right.color == RED:
                split(node)
                flag = False
            else:
                node = rotate_right(node)
    return node, flag

# 右部分木の修正
def balance_insert_right(node, flag):
    if flag: return node, flag
    if node.color == BLACK:
        flag = True
        # 右(赤)の子に赤があるか
        if node.right.left.color == RED:
            node.right = rotate_right(node.right)
        if node.right.right.color == RED:
            # 赤が 2 つ続く
            if node.left.color == RED:
                split(node)
                flag = False
            else:
                node = rotate_left(node)
    return node, flag

# 挿入
def insert(node, x):
    if node is null: return Node(x), False
    if x < node.data:
        node.left, flag = insert(node.left, x)
        return balance_insert_left(node, flag)
    elif x > node.data:
        node.right, flag = insert(node.right, x)
        return balance_insert_right(node, flag)
    return node, True

#
# データの削除
#

# 右部分木の修正
def balance_right(node, flag):
    if flag: return node, flag
    if node.left.left.color == BLACK and node.left.right.color == BLACK:
        if node.left.color == BLACK:
            # left is 2node
            node.left.color = RED
            if node.color == BLACK: return node, False
            node.color = BLACK
        else:
            # node is 3node
            node = rotate_right(node)
            node.right, _ = balance_right(node.right, False)
    else:
        # left is 3,4node
        if node.left.right.color == RED:
            node.left = rotate_left(node.left)
        node = rotate_right(node)
        node.right.color = BLACK
        node.left.color = BLACK
    return node, True

# 左部分木の修正
def balance_left(node, flag):
    if flag: return node, flag
    if node.right.left.color == BLACK and node.right.right.color == BLACK:
        # right is 2node
        if node.right.color == BLACK:
            # node is 2node
            node.right.color = RED
            if node.color == BLACK: return node, False
            node.color = BLACK
        else:
            # node is 3node
            node = rotate_left(node)
            node.left, _ = balance_left(node.left, False)
    else:
        # right is 3,4node
        if node.right.left.color == RED:
            node.right = rotate_right(node.right)
        node = rotate_left(node)
        node.left.color = BLACK
        node.right.color = BLACK
    return node, True

# 最小値を探す
def search_min(node):
    while node.left is not null: node = node.left
    return node.data

# 削除
def delete(node, x):
    if node is null: return node, True
    if x == node.data:
        if node.left is null and node.right is null:
            return null, node.color == RED
        elif node.right is null:
            node.left.color = BLACK
            return node.left, True
        elif node.left is null:
            node.right.color = BLACK
            return node.right, True
        else:
            node.data = search_min(node.right)
            node.right, flag = delete(node.right, node.data)
            return balance_right(node, flag)
    elif x < node.data:
        node.left, flag = delete(node.left, x)
        return balance_left(node, flag)
    else:
        node.right, flag = delete(node.right, x)
        return balance_right(node, flag)

#
# 巡回
#
def traverse(node):
    if node is not null:
        for x in traverse(node.left):
            yield x
        yield node.data
        for x in traverse(node.right):
            yield x

# # 木の表示
# def print_node(node, n):
#     color = ('B', 'R')
#     if node is not null:
#         print_node(node.left, n + 1)
#         print '    ' * n, color[node.color], node.data
#         print_node(node.right, n + 1)

# # 赤黒木の条件を満たしているか
# def check_rbtree(node):
#     if node is not null:
#         if node.color == RED:
#             if node.left.color == RED or node.right.color == RED:
#                 raise 'rbtree error1'
#         a = check_rbtree(node.left)
#         b = check_rbtree(node.right)
#         if a != b: raise 'rbtree error2'
#         if node.color == BLACK: a += 1
#         return a
#     return 0

# # test
# if __name__ == '__main__':
#     import random
#     root = make_null()
#     buff = range(1000)
#     random.shuffle(buff)
#     print 'insert test'
#     for x in buff:
#         root, _ = insert(root, x)
#         root.color = BLACK
#         check_rbtree(root)
#     print 'search test'
#     random.shuffle(buff)
#     for x in buff:
#         if not search(root, x):
#             raise 'search error'
#     print 'delete test'
#     for x in buff:
#         root, _ = delete(root, x)
#         root.color = BLACK
#         check_rbtree(root)