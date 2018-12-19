# 此段代码用于xlsx读写测试

import xlrd
import xlwt
from xlutils.copy import copy

url = "/Users/dabin/Downloads/customer/"# 路径替换成自己的文件夹路径


def xls_add_info(file_path, row):
    # 打开要提取信息的表
    readbook = xlrd.open_workbook(url)
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


count = 1
xls_add_info(url,count)