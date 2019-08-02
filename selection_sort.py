#!/usr/bin/env python
# coding: utf-8

#  list = [17, 20, 93, 54, 77, 31, 44, 55, 226]
#  下标索引：0   1   2   3   4   5    6   7   8
#  j = 0
#  min_index = 0  此时与下一个数0+1比较
#  list[0], list[min_index] = list[min_index], list[0]

#  j = 1
#  min_index = 1 此时与1+1比较
#  list[1], list[min_index] = list[min_index], list[1]
#  单多行注释就一个组合键：选中+Ctrl+/

def selection_sort(list):

    n = len(list)
    for j in range(n-1):  # j产生的是0～n-2的range,不是0~n
        min_index =j  # 6到14这段代码重复执行遍历,需要再添加一个外循环,先写内循坏，再写外循坏
        for i in range(j+1, n):
            if list[min_index] > list[i]:
                min_index = i
        list[j], list[min_index] = list[min_index], list[j]

if __name__ == "__main__":
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    print(li)
    selection_sort(li)
    print(li)