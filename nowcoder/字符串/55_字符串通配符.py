"""
55_字符串通配符 - 

给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。

Author: kayotin
Date 2024/4/20
"""


def re_test(s: str, p: str):
    """动态规划，dp[i][j]代表a字符串的前i是否能和p字符串的前j匹配"""
    n, m = len(p)+1, len(s)+1
    dp = [[False]*m for _ in range(n)]

    if s == 1:
        return

    # 初始化状态
    dp[0][0] = True
    # 以下这个是用来处理p字符中全是*的特殊情况
    for i in range(1, n):
        if p[i-1] == "*":
            dp[i][0] = True
        else:
            break

    for i in range(1, n):
        # 默认没有*
        is_star = False
        for j in range(1, m):
            # 如果p是*
            if p[i-1] == "*":
                # 上一行是t，这行全是t
                if dp[i-1][0]:
                    dp[i] = [True] * m
                # 如果上一行当前位置是t，则接下来都可以t
                if dp[i-1][j]:
                    is_star = True
                if is_star and s[j-1].isalnum():
                    dp[i][j] = True
            # 如是？或者字符相同，当前dp[i][j]是t
            elif p[i-1] == "?" or p[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[n-1][m-1]

