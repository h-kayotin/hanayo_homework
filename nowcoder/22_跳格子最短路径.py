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
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1

    print(dp[n][m])


def min_len_for_cells2(x: str, y: str):
    """跳格子：空间优化"""
    m, n = len(x), len(y)
    dp = [0] * (m + 1)

    # 初始化首行
    for j in range(1, m+1):
        dp[j] = j
    # 状态转移
    for i in range(1, n+1):
        leftup = dp[0]
        dp[0] += 1
        for j in range(1, m+1):
            temp = dp[j]
            if x[i-1] == y[i-1]:
                dp[j] = min(dp[j-1], dp[j], leftup) + 1
            else:
                dp[j] = min(dp[j]+1, dp[j-1]+1, leftup+2)
            leftup = temp
    return dp[m]

if __name__ == '__main__':
    min_len_for_cells1("ABACDE", "BCDAA")
    print(min_len_for_cells2("ABACDE", "BCDAA"))