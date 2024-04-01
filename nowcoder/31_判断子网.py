"""
31_判断子网 - 
给出子网掩码和2个ip地址，判断是否在一个网段

Author: hanayo
Date： 2024/4/1
"""

x = [255, 255, 255, 0]
y = [192, 168, 0, 1]
z = [192, 168, 0, 254]

# max(x+y+z)可以返回三个数组中最小的值
print(max(x ,y ,z))
print(min(x+y+z))


while True:
    try:
        x = [int(a) for a in input().split('.')]
        y = [int(a) for a in input().split('.')]
        z = [int(a) for a in input().split('.')]
        m, n = [], []
        if x[0] != 255 or x[3] != 0 or max(x+y+z) > 255 or min(x+y+z) < 0:
            print('1')
        else:
            for i in range(len(x)):
                m.append(int(x[i]) & int(y[i]))
                n.append(int(x[i]) & int(z[i]))
            if m == n:
                print('0')
            else:
                print('2')
    except EOFError:
        break
