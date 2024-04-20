"""
54_矩阵乘法的计算次数 - 

矩阵乘法 a矩阵 x行y列 c矩阵y行z列，实际计算次数是x*y*z

Author: kayotin
Date 2024/4/20
"""


n = int(input())
xys = []
for _ in range(n):
    x, y = str(input()).split(" ")
    xys.append((int(x), int(y)))
turn_str = str(input())

my_stack = []
res = 0
for c in turn_str:
    if c.isalpha():
        my_stack.append(xys[ord(c)-65])
    elif c == ")" and len(my_stack) >= 2:
        b = my_stack.pop()
        a = my_stack.pop()
        res += a[0]*a[1]*b[1]
        my_stack.append((a[0], b[1]))

print(res)

