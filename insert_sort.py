#!/usr/bin/env python
# coding: utf-8
def insert_sort(li):
    n = len(li)
    # 从右边无序序列取出多少个元素执行这样的过程
    for j in range(1,):
        # i代表内层循环的起始值
        i = j
        # 执行从右边无序的序列取出第一个元素,即i的位置的元素,然后将其插入正确的位置
        while i > 0:
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
                i -= 1
            else:
                break
            # i = j  j-1 j-2 ....1  即range(j,0,-1)  while条件可改为for i in range(j,0,-1)
if __name__ == "__main__":
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226, 0, 100]
    print(li)
    insert_sort(li)
    print(li)