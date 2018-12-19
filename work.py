#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import xlrd
import xlwt
from xlutils.copy import copy

"""
 要排查掉文件名有问题的文件：分别包含".DS_Store"、".idea"、“~”
"""

def xls_add_info(file_path, row):
  if ".DS_Store" not in  file_path and "idea" not in file_path:
    readbook = xlrd.open_workbook(file_path)
    sheet = readbook.sheet_by_index(0)  # 索引的方式，从0开始
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    lng = sheet.cell(1, 1).value  # 获取1行1列的表格值
    lat = sheet.cell(1, 7).value  # 获取1行1列的表格值

    # 写入部分
    rbook = xlrd.open_workbook("/Users/dabin/Downloads/xlsprogram/customer.xls")
    wbook = copy(rbook)
    w_sheet = wbook.get_sheet(0)
    w_sheet.write(row, 0, lng)
    w_sheet.write(row, 1, lat)
    wbook.save('customer.xls')
    print(lng)
    print(lat)



# 解析出所有文件路径
dirs = "/Users/dabin/Downloads/customer"

file_lists = []

# 列出所有文件路径


def file_paths(file_dirs):
    # row = 0
    for fpathe, dirs, fs in os.walk(file_dirs):
        for f in fs:
            # 路径
            if ".DS_Store" not in  f and ".idea" not in f and "~$" not in f:
              file_lists.append(os.path.join(fpathe, f))
            # xls_add_info(file_path, row)
            # print(file_path)
            # print('\n')
            # print('添加成功')
            # row += 1


file_paths(dirs)
count_end=0
for x in file_lists[:100]:
  print(x)
  print(count_end)
  count_end+=1


row = 0
for f in file_lists:
    xls_add_info(f, row)
    row += 1
