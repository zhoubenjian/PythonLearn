"""
查找 - 顺序查找和二分查找
算法：解决问题的方法（步骤）
评价一个算法的好坏主要有两个指标：渐近时间复杂度和渐近空间复杂度，通常一个算法很难做到时间复杂度和空间复杂度都很低（因为时间和空间是不可调和的矛盾）
表示渐近时间复杂度通常使用大O标记
O(c)：常量时间复杂度 - 哈希存储 / 布隆过滤器
O(log_2 n)：对数时间复杂度 - 折半查找
O(n)：线性时间复杂度 - 顺序查找
O(n * log_2 n)：- 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
O(n ** 2)：平方时间复杂度 - 简单排序算法（冒泡排序、选择排序、插入排序）
O(n ** 3)：立方时间复杂度 - Floyd算法 / 矩阵乘法运算
也称为多项式时间复杂度
O(2 ** n)：几何级数时间复杂度 - 汉诺塔
O(3 ** n)：几何级数时间复杂度
也称为指数时间复杂度
O(n!)：阶乘时间复杂度 - 旅行经销商问题 - NP
"""



'''顺序查找'''
def seq_index(items: list, elem) -> int:
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1

'''二分查找'''
def bin_search(items, elem):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1
        
    