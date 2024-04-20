"""
46_放苹果全排列 - 
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。
Author: kayotin
Date 2024/4/12
"""


def put_apple(m: int, n: int):
    """动态规划"""
    # dp[i][j]表示i个苹果放在j个盘子的最多方法
    dp = [[0]*(n+1) for _ in range(m+1)]

    # 初始化
    # 显然0个或1个苹果放n个盘子都只有1种方案
    for j in range(1, n+1):
        dp[0][j] = 1
        dp[1][j] = 1
    # 同样，1个盘子放任何苹果都只有1种方案
    for i in range(1, m+1):
        dp[i][1] = 1

    # 状态转移
    for i in range(2, m+1):
        for j in range(2, n+1):
            # 苹果小于盘子时，多出的盘子都是空的没有意义的
            if i < j:
                dp[i][j] = dp[i][i]
            # 苹果数量>盘子时，有2种情况。dp[i][j]就是这2个情况之和
            # 1.所有盘子都至少有一个苹果，也就是i-j， dp[i-j][j]
            # 2.至少空一个盘子，也就是i-1， dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-j][j]
    print(dp[m][n])


put_apple(7, 3)
