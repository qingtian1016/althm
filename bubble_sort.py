#!/usr/bin/env python
# coding: utf-8
def bubble_sort(li):
    n = len(li)
    for j in range(1, n-1):
        for i in range(n-j):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]


if __name__ == "__main__":
    li = [54, 2, 15, 16, 4, 99, 75, 55, 100]
    print(li)
    bubble_sort(li)
    print(li)
