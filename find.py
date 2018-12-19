# 此段代码用于读取所有文件路径
import os

# 解析出所有文件路径
dirs = "/Users/mac/Downloads/customer"

file_lists = []

# 列出所有文件路径


def file_paths(file_dirs):
    # row = 0
    for fpathe, dirs, fs in os.walk(file_dirs):
        for f in fs:
            # 路径
            # if ".DS_Store" not in  f and ".idea" not in f and "~$" not in f:
            file_lists.append(os.path.join(fpathe, f))


file_paths(dirs)
for x in file_lists:
    print(x)
