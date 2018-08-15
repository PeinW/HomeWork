#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
print(' 杨辉三角 '.center(97, '*'))
triangle = []
for n in range(10):
    temp = copy.copy(triangle)
    for i in range(1, len(temp)):
        triangle[i] = temp[i] + temp[i-1]
    triangle.append(1)
    print(str(triangle).replace('[', '').replace(']', '').replace(',', ' ').center(100, '*'))

print('hhhhhh',end='')
print('hhhhhh')
print('hhhhhh')
print('hhhhhh')
print('hhhhhh')



# print('================== 闰年 ====================')
#
# rec = 'a'
#
# while (not rec.isdigit()) or (int(rec) < 0):
#     rec = input('请输入一个年份：')
#
# rec = int(rec)
# if rec % 4 == 0:
#     if rec % 100 == 0:
#         if rec % 400 ==0:
#             print('%s年是闰年' % rec)
#         else:
#             print('%s年不是闰年' % rec)
#     else:
#         print('%s年是闰年' % rec)
# else:
#     print('%s年不是闰年' % rec)


# print('================== 水仙数 ====================')
#
# rec = 1
# while (rec > 999) or (rec < 99):
#     rec = input('请输入一个三位数的正整数')
#     rec = int(rec)
#
# a = int(rec / 100)
# b = int((rec - a*100) / 10)
# c = rec % 10
# print('百位是：%s' % a)
# print('十位是：%s' % b)
# print('个位是：%s' % c)
#
# temp = pow(a, 3) +pow(b, 3) +pow(c, 3)
#
# if temp == rec:
#     print('This number %s is 水仙数' % rec)
# else:
#     print('This number %s is not 水仙数' % rec)