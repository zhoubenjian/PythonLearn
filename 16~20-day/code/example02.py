def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


# 函数的设计要尽量做到无副作用（不影响调用者）
# 9 1 2 3 4 5 6 7 8
# 9 2 3 4 5 6 7 8 1
# *前面的参数叫位置参数，传参时只需要对号入座即可
# *后面的参数叫命名关键字参数，传参时必须给出参数名和参数值
# *args - 可变参数 - 元组
# **kwargs - 关键字参数 - 字典
def bubble_sort(origin_items, *, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = origin_items[:]
    for i in range(1, len(items)):
        swapped = False
        for j in range(i - 1, len(items) - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - i - 1, i - 1, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    result1 = bubble_sort(items)
    print(result1)
    
    print('*********************************')
    
    result2 = bubble_sort(items)
    print(result2)
    
    
if __name__ == '__main__':
    main()