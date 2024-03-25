"""
22_跳格子最短路径 - 

Author: hanayo
Date： 2024/3/25
"""


def min_len_for_cells1(x: str, y: str):
    m, n = len(x), len(y)
    dp = [[0] * (m + 1) for i in range(n + 1)]
    # dp[i,j]表示(0,0) 到(i.j)的最短距离，有三种情况，这三者取最小
    # 1：dp[i-1][j-1] + 1或2 取决于是否有斜线
    # 2： dp[i-1][j] + 1
    # 3： dp[i][j-1] +1

    # 先考虑第一行的情况
    for j in range(1, m + 1):
        dp[0][j] = j
    # 第一列，其实也一样
    for i in range(1, n + 1):
        dp[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 第一种情况
            if x[j - 1] == y[i - 1]:
                dp1 = dp[i - 1][j - 1] + 1
            else:
                dp1 = dp[i - 1][j - 1] + 2

            # 第二种情况
            dp2 = dp[i - 1][j] + 1
            # 第三种情况
            dp3 = dp[i][j - 1] + 1
            dp[i][j] = min([dp1, dp2, dp3])

    print(dp[n][m])


def step_for_cells(x: str, y: str):
    m, n = len(x), len(y)
    dp = []
    for i in range(n):
        row_list = []
        for j in range(m):
            if x[j] == y[i]:
                row_list.append(j)
        dp.append(row_list)
    print(dp)
    res_list = []
    for row in dp:
        if not row:
            continue
        else:
            # 每一行取值逻辑，这一行中第一个比当前值大，
            pass


if __name__ == '__main__':
    step_for_cells("ABACDE", "BCDAA")