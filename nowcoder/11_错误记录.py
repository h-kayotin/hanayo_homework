"""
11_错误记录 -
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：

1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是“相同”的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。也就是说，哪怕不同路径下的文件，如果它们的名字的后16个字符相同，也被视为相同的错误记录
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准

Author: kayotin
Date 2024/3/21
"""

res_list = list()
delete_list = set()


def input_value():
    file_with_path, line_num = str(input()).split(" ")
    filename = file_with_path.split("\\")[-1][-16:]
    return filename, line_num


def check_err(filename, line_num):
    err_log = f"{filename} {line_num}"
    # 判断是否之前记录过，已经出现过不再记录
    if err_log in delete_list:
        return

    # 对结果列表进行遍历,如果已经有了，那么值加一，结束check
    for res in res_list:
        if err_log == res[0]:
            res[1] += 1
            return
    # 当前默认是新值，如果列表已经是8，删除一个再加入
    if len(res_list) == 8:
        delete_res = res_list.pop(0)
        delete_list.add(delete_res[0])
    res_list.append([err_log, 1])


def main():
    while True:
        filename, line_num = input_value()
        check_err(filename, line_num)


try:
    main()
except (EOFError, ValueError):
    pass

for res in res_list:
    print(res[0], res[1])
