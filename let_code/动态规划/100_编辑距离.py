"""
100_编辑距离 - 
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
Author: hanayo


https://leetcode.cn/problems/edit-distance/solutions/6455/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/?envType=study-plan-v2&envId=dynamic-programming
Date： 2024/6/27
"""


def min_distance(self, word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    # 引入第一个空字符，所以是+1
    dp = [[0]*(m+1) for _ in range(n+1)]
    # 初始化首行，首行首列相当于直接删除
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + 1
    # 初始化首列
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + 1

    # 状态转移
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # 分别对应 替换 删除 插入
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    return dp[n][m]